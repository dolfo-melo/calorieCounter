/* Algoritmo
    1 - Digitar a calorias do alimento;
    2 - Definir a refeição a qual se refere;
    3 - Calcular ou Limpar as Calorias;
    4 - Exibir as calorias por refeição;
    5 - Exibir as calorias totais.
*/

// Definindo as variáveis
const calourieCounter = document.getElementById('calorie-counter');
const budgetNumberInput = document.getElementById('budget');
const entryDropdown = document.getElementById('entry-dropdown');
const clearButton = document.getElementById('clean');
const output = document.getElementById('output');

let isError = false;

// Tratamento de entrada de dados e erros

    // Padronização de entrada de dados
function clearInputString(str){
    const regex = /[\+-\s]/g;
    return str.replace(regex, '')
}

   // Tratamento para números exponenciais
function invalidCharacteres(str){
    const regex = /[0-9]e[0-9]]/g;
}


// 1 - Digitar calorias do alimento
    // Função para pegar o número de calorias e destinguir a qual refeição se refere
    
function enterCalorie(){
    calorieCounter = prompt('Digite a caloria da sua refeição: ');
    if(entryDropdown.value == breakfast){
        
    }
    output += calorieCounter;
}

function calculateCalories(){
    output.innerText = output;
}
