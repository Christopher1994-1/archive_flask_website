alert("type in 'ann', 'bill' or 'mine' to filter through images")


let searchBox = document.querySelector('#search-box');
let images = document.querySelectorAll('.s-container .s-image-container .s-image');

searchBox.oninput = () =>{
    images.forEach(hide => hide.style.display = 'none'); // hides the images once user types in input
    let value = searchBox.value
    images.forEach(filter =>{
        let title = filter.getAttribute('data-title');
        if(value == title){
            filter.style.display = 'block'
        }
        if(searchBox.value == ''){
            filter.style.display = 'block'
        }
    });
};