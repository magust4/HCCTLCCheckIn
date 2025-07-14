// Get the stored student ID from localStorage
const studentId = localStorage.getItem("studentId");

// Make sure the student ID exists — otherwise, redirect back
if (!studentId) {
  alert("Student ID not found. Redirecting to login.");
  window.location.href = "index.html";
}

// Select all buttons in the grid
const buttons = document.querySelectorAll(".grid button");

// Add click event to each button
buttons.forEach(button => {
  button.addEventListener("click", () => {
    const selectedOption = button.textContent.trim();
    const date = new Date().toISOString().split('T')[0]; // e.g., "2025-07-02"

    fetch("http://localhost:8000/submit", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        date,
        studentId,
        selectedOption
      })
    })
    .then(response => {
      if (!response.ok) throw new Error("Failed to submit");
      return response.json();
    })
    .then(() => {
      alert("✅ Check-in successful! Thank you.");
      localStorage.removeItem("studentId"); // Clear the ID after use
      window.location.href = "../index/index.html";  // Redirect to login or home
    })
    .catch(err => {
      console.error("Submission error:", err);
      alert("⚠️ Something went wrong. Please try again.");
    });
  });
});
