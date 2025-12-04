const table = document.getElementById("bodyTable");
const container = document.getElementById("container");

document.addEventListener("DOMContentLoaded", async function () {
  load().then((result) => {
    Object.entries(result).forEach(([key, value]) => {
      value.forEach((valuesArray) => {
        const tr = document.createElement("tr");

        valuesArray.forEach((value) => {
          const td = document.createElement("td");
          td.setAttribute("class", "tdTableProducts");
          td.textContent = value;
          tr.appendChild(td);
        });

        table.appendChild(tr);
      });

      addButtom();
    });
  });
});

async function load() {
  try {
    const dataProduct = await fetch("http://127.0.0.1:8080/");
    const result = await dataProduct.json();

    return result;
  } catch (err) {
    return err;
  }
}

function addButtom() {
  const nextElement = table.children;
  const p = document.createElement("p");

  for (const next of nextElement) {
    const button = document.createElement("button");
    button.setAttribute("class", "deleteButton");
    button.textContent = "delete";

    button.addEventListener("click", (event) => {
      const filaPadre = event.target.closest("tr");
      event.target.disabled = true;

      if (filaPadre) {
        const index = filaPadre.textContent.trim().slice(0, 2); //not is number is remove
        const indexId = letterDetector(index);

        fetch(`http://127.0.0.1:8080/api/delete_product/${indexId}`, {
          method: "Delete",
        })
          .then((response) => {
            if (response.ok) {
              return response.json();
            } else {
              return "The procut not finding";
            }
          })
          .then((data) => {
            if (data) {
              Object.values(data).forEach((value) => {
                alert(value);
              });

              filaPadre.remove();
              location.reload(true);
            } else {
              alert("It is not possible to remove the product");
              event.target.disabled = false;
            }

            container.firstChild(p);
          });
      }
    });
    next.appendChild(button);
  }
}
