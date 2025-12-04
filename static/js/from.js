const form = document.getElementById("from_product");

const nameProcduct = document.getElementById("name");
const purchase_cost = document.getElementById("purchase_cost");
const shipping_cost = document.getElementById("shipping_cost");
const sale = document.getElementById("sale");

form.addEventListener("submit", async function (e) {
  e.preventDefault();

  const datos = {
    name: nameProcduct.value,
    purchase_cost: purchase_cost.value,
    shipping_cost: shipping_cost.value,
    sale: sale.value,
  };

  await fetch("http://127.0.0.1:8080/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },

    body: JSON.stringify(datos),
  })
    .then((response) => {
      if (response.status == 200) {
        window.location.href = "http://127.0.0.1:8080/home";
      }
    })
    .catch((erro) => {
      console.error("Error de red:", erro);
    });
});
