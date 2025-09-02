function exampleJSFunction(arr, callback) {
    arr.push(100);
    callback();
}

var arr = ["Juan", "Karla", "Ricardo", "Pedro"];

exampleJSFunction(arr, function() {
    console.log(arr);
});

// In JavaScript, a callback is a function that is passed as an argument to another function, 
// and is then executed inside that outer function at a later point. 