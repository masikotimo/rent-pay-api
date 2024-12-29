class USSDMenuService:
    def __init__(self, session, text):
        self.session = session
        self.text = text
        self.menu_steps = text.split('*') if text else []

    def process(self):
        if not self.text:
            return self.main_menu()
        
        current_menu = self.session.current_menu
        if current_menu == 'MAIN':
            return self.handle_main_menu()
        elif current_menu == 'CHECK_BALANCE':
            return self.handle_balance_check()
        elif current_menu == 'PAYMENT':
            return self.handle_payment()
        
        return self.main_menu()

    def main_menu(self):
        self.session.current_menu = 'MAIN'
        self.session.save()
        return "CON Welcome to Property Management\n1. Check Balance\n2. Make Payment\n3. Exit"

    def handle_main_menu(self):
        choice = self.menu_steps[-1]
        if choice == '1':
            self.session.current_menu = 'CHECK_BALANCE'
            self.session.save()
            return "CON Enter your tenant reference number:"
        elif choice == '2':
            self.session.current_menu = 'PAYMENT'
            self.session.save()
            return "CON Enter your tenant reference number:"
        elif choice == '3':
            return "END Thank you for using our service"
        return "END Invalid choice"

    def handle_balance_check(self):
        reference = self.menu_steps[-1]
        try:
            tenant = self.session.tenant or Tenant.objects.get(reference_number=reference)
            self.session.tenant = tenant
            self.session.save()
            return f"END Your current balance is: {tenant.balance}"
        except Tenant.DoesNotExist:
            return "END Invalid reference number"

    def handle_payment(self):
        if len(self.menu_steps) == 2:
            reference = self.menu_steps[-1]
            try:
                tenant = self.session.tenant or Tenant.objects.get(reference_number=reference)
                self.session.tenant = tenant
                self.session.save()
                return f"CON Enter amount to pay:"
            except Tenant.DoesNotExist:
                return "END Invalid reference number"
        
        elif len(self.menu_steps) == 3:
            try:
                amount = float(self.menu_steps[-1])
                return "CON Confirm payment:\n1. Yes\n2. No"
            except ValueError:
                return "END Invalid amount"
        
        elif len(self.menu_steps) == 4:
            choice = self.menu_steps[-1]
            if choice == '1':
                # Payment processing logic would go here
                return "END Payment initiated. You will receive a prompt to complete the payment."
            elif choice == '2':
                return "END Payment cancelled"
            return "END Invalid choice"
        
        return "END Invalid input"