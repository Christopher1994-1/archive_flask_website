const fs = require('fs')
let path = "C:/Users/yklac/Desktop/projects/git_projects/flask_website/flask_site/static/images/search_images/1.jpg"

fs.readFile(path, (err, data) => {
    if (err){
        console.log(err);
    }
    console.log(data.toString());
});