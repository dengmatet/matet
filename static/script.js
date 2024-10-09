var x = document.getElementById("login");
var y = document.getElementById("sign-up");
var z = document.getElementById("btn");
var modal = document.getElementById("show-form");

function signup() {
  x.style.left = "-400px";
  y.style.left = "50px";
  z.style.left = "110";
}
function login() {
  x.style.left = "50px";
  y.style.left = "450px";
  z.style.left = "0";
}
window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};

// Search engin get
let input = document.querySelector("input");
input.addEventListener("input", async function () {
  let Response = await fetch("/search?search=" + input.value);
  let shows = await Response.text();
  document.querySelector("").innerHTML = shows;
});

// Start with first post
let counter = 1;

// Load posts 20 at a time
const quantity = 20;

// When DOM loads, render the first 20 posts
document.addEventListener("DOMContentLoaded", load);

window.onscroll = () => {
  if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
    load();
  }
};

// Load next set of posts
function load() {
  // Set start and end post number, and update counter
  const start = counter;
  const end = start + quantity - 1;
  counter = end + 1;

  // Get new posts and add posts
  fetch("/posts?start=${start}&end=${end}")
    .then((Response) => Response.json())
    .then((data) => {
      data.posts.forEach(add_post);
    });
}

// Add a new post with given content to DOM
function add_post(content) {
  //Create new post
  const post = document.createElement("div");
  post.className = "post";
  post.innerHTML = contents;

  // Add post to DOM
  document.querySelector("posts").append(post);
}
