function valida_CadastroFuncionario() {
    var iNome = document.getElementById("iNome").value;
    var nCpf = document.getElementById("nCpf").value;
    var dataNascimento = document.getElementById("dataNascimento").value;
    var nMatricula = document.getElementById("nMatricula").value;
    var cCargo = document.getElementById("cCargo").value;

    if (iNome.length == "") {
        alert("Preencha o campo nome!")
        return false;
    }
    else if (nCpf.length == "") {
        alert("Preencha o campo CPF!")
        return false;
    }
    else if (dataNascimento.length == "") {
        alert("Preencha o campo Data de Nascimento!")
        return false;
    }
    else if (nMatricula.length == "") {
        alert("Preencha o campo Nº Matrícula!")
        return false;
    }
    else if (cCargo.length == "") {
        alert("Preencha o campo Cargo!")
        return false;
    }

}