const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

console.log('Building ChittrChattr...');

try {
  // Run Tailwind CSS build
  console.log('Compiling Tailwind CSS...');
  execSync('npx tailwindcss -i ./src/index.css -o ./src/tailwind-output.css', { stdio: 'inherit' });
  
  // Run React build
  console.log('Building React app...');
  execSync('npx react-scripts build', { stdio: 'inherit' });
  
  console.log('Build completed successfully!');
} catch (error) {
  console.error('Build failed:', error.message);
  process.exit(1);
}
