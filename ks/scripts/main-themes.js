
// ENTERING THE THEME
function enterTheme() {
    let input = document.getElementById("myTheme");
    value = input.value;
    localStorage.setItem("theme", value);
    window.location.href = "clothing.html"
}

// Clears local storage
function clearTheme() {
    //let value = "Your Theme";
    //localStorage.setItem("theme", value);
    localStorage.clear()
    document.getElementById('myTheme').value = ''
}

// USES THE INNERTEXT TO CREATE THE THEME VARIABLE
// Get all the link elements
const links = document.querySelectorAll(".themeItem");

// Add a click event listener to each link
links.forEach(link => {
    link.addEventListener("click", handleClick);
})

// Click event handler
function handleClick(event) {
    event.preventDefault(); // Prevent default link behavior

    // Get the innerText of the clicked link and store it in a variable
    clickedLinkText = event.target.innerText;

    localStorage.setItem("theme", clickedLinkText);
    window.location.href = "clothing.html"
}

// Displays the results
let themeOutput = localStorage.getItem("theme");
let output = document.getElementById("themeBox");
let outputPerfectOutfit = document.getElementById("themePerfectOutfit");
output.innerText = themeOutput;
outputPerfectOutfit.innerText = themeOutput;

// END OF: ENTERING THE THEME

