for (const element of document.getElementsByClassName("box")) {
  element.addEventListener("click", async () => {

    if (element.children.length > 0) return;

    // PLAYER (O)
    const imageO = document.createElement("img");
    imageO.src = "assets/img/o.png";
    element.appendChild(imageO);

    const id = element.id.match(/(\d+)$/)[0];

    try {
      const response = await fetch(`http://localhost:8000?id=${id}`, {
        method: "POST",
      });

      if (!response.ok) return;

      const data = await response.json();
      const { cpu_move, winner } = data;

      // CPU (X)
      if (cpu_move !== "") {
        const box = document.getElementById(`box${cpu_move}`);
        if (box && box.children.length === 0) {
          const imageX = document.createElement("img");
          imageX.src = "assets/img/x.png";
          box.appendChild(imageX);
        }
      }

      // ESITO
      if (winner === "CPU") {
        alert("HA VINTO LA CPU");
      } else if (winner === "PLAYER") {
        alert("HAI VINTO");
      }

      if (winner) {
        const check = confirm("VUOI RIGIOCARE?");
        if (check) {
          await fetch("http://localhost:8000/reset_tris", {
            method: "POST",
          });
        }
        window.location.reload();
      }
      winner = "";
    } catch (error) {
      console.error(error);
    }
  });
}
