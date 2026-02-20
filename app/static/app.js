async function loadUsers() {
    const response = await fetch("/users/");
    const users = await response.json();

    const list = document.getElementById("userList");
    list.innerHTML = "";

    users.forEach(user => {
        const li = document.createElement("li");
        li.textContent = user.name;
        list.appendChild(li);
    });
}

async function createUser() {
    const name = document.getElementById("name").value;

    await fetch("/users/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name })
    });

    document.getElementById("name").value = "";
    loadUsers();
}

window.onload = loadUsers;