
let searchBox = document.querySelector('#search-box');
let image = document.querySelectorAll('.s-container .s-image-container .s-image');

searchBox.oninput = () =>{
    image.forEach(hide => hide.style.display = 'none'); // hides the images once user types in input
    let value = searchBox.value
    image.forEach(filter =>{
        let title = filter.getAttribute('data-title');
        if(value == title){
            filter.style.display = 'block'
        }
        if(searchBox.value == ''){
            filter.style.display = 'block'
        }
    });
};

// ***************************************************************************************************
// pagination code:

var fs = require('fs');
var path = "C:/Users/yklac/Desktop/projects/git_projects/flask_website/flask_site/static/images/search_images"
var files = fs.readdirSync(path);
console.log(files)

document.getElementById('maina').innerHTML = files