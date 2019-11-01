function valida_cadastro_vendas() {
    var dataVenda = document.getElementById("dataVenda").value;
    var nContrato = document.getElementById("nContrato").value;
    var iTipoContrato = document.getElementById("iTipoContrato").value;
    var cTipoPagamento = document.getElementById("cTipoPagamento").value;
    var cCliente = document.getElementById("cCliente").value;
    var cFuncionario = document.getElementById("cFuncionario").value;

    if (dataVenda.length == "") {
        alert("Preencha o campo Data da Venda!")
        return false;
     } else if (nContrato.length == "") {
        alert("Preencha o campo contrato!")
        return false;
    } else if (iTipoContrato.length == "") {
        alert("Preencha o tipo contrato!")
        return false;
    } else if (cTipoPagamento.length == "") {
        alert("Preencha o tipo pagamento!")
        return false;
    } else if (cCliente.length == "") {
        alert("Preencha o código cliente!")
        return false;
    } else if (cFuncionario.length == "") {
        alert("Preencha o código Funcionário!")
        return false;
    } 
}






