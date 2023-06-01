let currentExpression = ''

function appendNumber(number) {
  currentExpression += number
  updateResult()
}

function appendOperator(operator) {
  currentExpression += operator
  updateResult()
}

function calculate() {
  try {
    const result = eval(currentExpression)
    document.getElementById('result').value = result
  } catch (error) {
    console.error('Erro ao calcular expressão:', error)
    document.getElementById('result').value = 'Erro'
  }
}

function clearResult() {
  currentExpression = ''
  updateResult()
}

function updateResult() {
  document.getElementById('result').value = currentExpression
}

function updateClock() {
  const now = new Date()
  const hours = String(now.getHours()).padStart(2, '0')
  const minutes = String(now.getMinutes()).padStart(2, '0')
  const seconds = String(now.getSeconds()).padStart(2, '0')
  const time = `${hours}:${minutes}:${seconds}`
  document.getElementById('clockDisplay').textContent = time
}

setInterval(updateClock, 1000)
