

document.addEventListener("DOMContentLoaded", function() {
    let currentLevel = 1; // Default level

    // Update the level based on the current URL if applicable
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.has('level')) {
        currentLevel = urlParams.get('level');
        document.getElementById("levelSelector").value = currentLevel;
    }

    // Listen for changes to the dropdown and update the level
    document.getElementById("levelSelector").addEventListener("change", function(event) {
        currentLevel = event.target.value;
        window.location.href = `/chords?level=${currentLevel}`; // Redirect based on level
    });

    // Fetch chord based on selected level
    document.getElementById("generateChord").addEventListener("click", function() {
        fetch(`/api/get_random_chord/${currentLevel}/`)
        .then(response => response.json())
        .then(data => {
            // Handle the data (display chord, play sound, etc.)
        })
        .catch((error) => console.error('There was an error!', error));
    });
});
