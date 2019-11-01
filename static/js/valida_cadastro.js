function valida_cadastro() {
    var iNome = document.getElementById("iNome").value;
    var iEmail = document.getElementById("iEmail").value;
    var nCpf = document.getElementById("nCpf").value;
    var nCel = document.getElementById("nCel").value;
    var dataNascimento = document.getElementById("dataNascimento").value;
    // DATA CADASTRO CLIENTE NÃO PRECISA DIGITAR
    var dataCadastro = document.getElementById("dataCadastro").value;
    var iEndereco = document.getElementById("iEndereco").value;
    var nCep = document.getElementById("nCep").value;
    var iBairro = document.getElementById("iBairro").value;
    var cUf = document.getElementById("cUf").value;
    var cDDD = document.getElementById("cDDD").value;
    var nTelefone = document.getElementById("nTelefone").value;
    // DATA ATUALIZAÇÃO ENVIAR AUTOMATICAMENTE TAMBÉM 
    var dataAtualizacao = document.getElementById("dataAtualizacao").value;

    // var dados = document.getElementById("iNome").value;

    // if(document.getElementById("iNome").value == "") {
    if (iNome.length == "") {
        alert("Preencha o campo nome!")
        return false;
     }
    else if (iEmail.length == "") {
        alert("Preencha o campo emai!")
        return false;
    }

    else if (nCpf.length == "") {
        alert("Preencha o campo CPF!")
        return false;
    }
    
    else if (nCel.length == "") {
        alert("Preencha o campo Celular!")
        return false;
    }
    else if (dataNascimento.length == "") {
        alert("Preencha o campo Data de Nascimento!")
        return false;
    }
    
    // campo data de cadastro deverá retornar a data atual. Sem precisar o cliente escrever
    else if (dataCadastro.length == ""){
        alert("Preencha data de Cadastro")
        return false;
    }
    else if (iEndereco.length == "") {
        alert("Preencha o campo Endereço!")
        return false;
    }
    else if (nCep.length == "") {
        alert("Preencha o campo CEP!")
        return false;
    
    }
    else if (iBairro.length == "") {
        alert("Preencha o campo Bairro!")
        return false;
    
    }
    
    else if (cUf.length == "") {
        alert("Preencha o campo UF!")
        return false;
    
    }    
    else if (cDDD.length == "") {
        alert("Preencha o campo DD!")
        return false;
    
    }
    
    else if (nTelefone.length == "") {
        alert("Preencha o campo Telefone!")
        return false;
    
    }
    
    // Campo não necessário
    else if (dataAtualizacao.length == "") {
        alert("Preencha o campo Data de Atualização!")
        return false;
    }
}






