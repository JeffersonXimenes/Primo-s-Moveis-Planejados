function redirectInicial(){			
    if (document.getElementById("nome").value == "gerente") {
        window.location.href = "Funcionarios/Inicial_Gerente.html";
    }

    else if (document.getElementById("nome").value == "cliente") {
        window.location.href = "Clientes/Inicial_Cliente.html";
    }

    else if (document.getElementById("nome").value == "funcionario") {
        window.location.href = "Funcionarios/Inicial_Funcionario.html";
    }           		 
}	