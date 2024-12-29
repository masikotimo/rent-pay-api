import express from 'express';
import { PythonShell } from 'python-shell';

const app = express();
const port = process.env.PORT || 8000;

// Start Django server
PythonShell.run('manage.py', {
  args: ['runserver', '0.0.0.0:8000']
}, (err) => {
  if (err) throw err;
  console.log('Django server is running on port 8000');
});

app.listen(port, () => {
  console.log(`Node server is running on port ${port}`);
});