function getWeatherData() {
    fetch('http://127.0.0.1:8000/api/history/all/')
    .then(response => response.json())
    .then(data => {
        // Selecionar os elementos HTML pelos seus IDs e preencher com os dados da API
        document.getElementById('weather').innerText = `Tempo: ${data.temperatura} °C`;
        document.getElementById('pressure').innerText = `Pressão Atmosférica: ${data.condicao}`;
        document.getElementById('humidity').innerText = `Umidade: ${data.umidade}%`;
        // Supondo que 'porcentagem_precipitacao' é o nome do campo correspondente na API
        document.getElementById('precipitation').innerText = `Porcentagem de Precipitação: ${data.porcentagem_precipitacao}%`;
        // Supondo que 'condicao_tempo' é o nome do campo correspondente na API
        document.getElementById('weather-condition').innerText = `Condição do Tempo: ${data.condicao_tempo}`;
    })
    .catch(error => {
        console.error('Erro ao buscar dados da API:', error);
    });
}

// Chamar a função quando a página for carregada
window.onload = function() {
    getWeatherData();
};
