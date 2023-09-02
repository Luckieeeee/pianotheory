document.addEventListener('DOMContentLoaded', (event) => {
    const correctAnswer = document.getElementById("correct-answer").value;
    const chordButtons = document.querySelectorAll(".chord-button");

    chordButtons.forEach(button => {
        button.addEventListener("click", function() {
            const selectedChordType = this.getAttribute("data-chord-type");
            
            if(selectedChordType === correctAnswer) {
                alert("Correct!");
            } else {
                alert("Incorrect. Try again.");
            }
        });
    });
});
