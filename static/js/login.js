const from_login = document.getElementById("from_login");
const name_user = document.getElementById("name");
const password_user = document.getElementById("password");
const send_login = document.getElementById("send_login");



send_login.addEventListener("submit", async(e)=> {
    e.preventDefault();
  
    const datos = {
        name_user:name_user.value,
        password:password_user.value
    }

    await fetch("http://127.0.0.1:8080/user", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },

    body: JSON.stringify(datos),

  })
    
  .then((response) => {
    response.json().then((data)=> {
        console.log(data)
    })
    
    //   if (response.status == 200) {
    //     window.location.href = `http://127.0.0.1:8080/${}`;
    //   }
    // }

})

    .catch((erro) => {
      console.error("Error de red:", erro);
    });

})