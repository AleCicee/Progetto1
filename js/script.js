for (const element of document.getElementsByClassName("box")) {
    element.addEventListener("click", () => {
        const id = element.id.match(/(\d+)$/)[0];
        fetch(`http://localhost:8000?id=${id}`, { method: "POST" });

        const image = document.createElement("img");
        image.src = "assets/img/o.png";
        element.appendChild(image);
    });
}
