let queue = 0;
let violations = 0;

// Simulate AI updates every 2 seconds
setInterval(() => {
  queue = Math.floor(Math.random() * 15) + 1;

  if (Math.random() > 0.7) {
    violations += 1;
  }

  document.getElementById("queueCount").innerText = queue;
  document.getElementById("violationCount").innerText = violations;
}, 2000);
