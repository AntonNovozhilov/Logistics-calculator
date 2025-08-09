const addBtn = document.getElementById('add-points-btn');
const additionalContainer = document.getElementById('additional-points');

let currentPoints = 2;
const MAX_POINTS = 10;

function createPointField(index) {
  const wrapper = document.createElement('div');
  wrapper.className = 'point-field';

  const label = document.createElement('label');
  label.htmlFor = `point-${index}`;
  label.textContent = `Точка ${index}`;

  const input = document.createElement('input');
  input.type = 'text';
  input.id = `point-${index}`;
  input.name = `point-${index}`;
  input.placeholder = 'Введите адрес или название';

  wrapper.appendChild(label);
  wrapper.appendChild(input);

  return wrapper;
}

function createPairRow(i) {
  const row = document.createElement('div');
  row.className = 'added-pair';

  const left = createPointField(i);
  const right = createPointField(i + 1);

  const removeBtn = document.createElement('button');
  removeBtn.type = 'button';
  removeBtn.className = 'remove-btn';
  removeBtn.title = 'Удалить эти точки';
  removeBtn.textContent = 'Удалить';
  removeBtn.addEventListener('click', () => {
    currentPoints -= 2;
    row.remove();
    if (addBtn) addBtn.disabled = currentPoints >= MAX_POINTS;
  });

  row.appendChild(left);
  row.appendChild(right);
  row.appendChild(removeBtn);

  return row;
}

if (addBtn) {
  addBtn.addEventListener('click', () => {
    if (currentPoints >= MAX_POINTS) return;
    const nextIndex = currentPoints + 1;
    const pair = createPairRow(nextIndex);
    additionalContainer.appendChild(pair);
    currentPoints += 2;
    if (currentPoints >= MAX_POINTS) {
      addBtn.disabled = true;
      addBtn.title = 'Достигнут максимум точек';
      addBtn.setAttribute('aria-disabled', 'true');
      addBtn.style.opacity = '0.6';
      addBtn.style.cursor = 'not-allowed';
    }
  });
}

if (addBtn) {
  addBtn.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      addBtn.click();
    }
  });
}
