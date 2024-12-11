const url = window.location.href;

console.log(url);

const nav_links = document.querySelectorAll(".nav-link");
nav_links.forEach(link => {
    if (link.href === url) {
        link.classList.add("active");
    }
});

