# ProducerConsumer-WithConcurrencyControl
Simple producer-consumer system using guarded blocks for concurrency control

---

# Solução da Tarefa

Implementamos a solução do problema clássico de Produtor-Consumidor em **Java** (fornecido) e em **Python** (`main.py`).

## Implementação em Java
A sincronização é feita na classe `Drop` utilizando `synchronized`, `wait()` (enquanto a condição de estado não é atendida) e `notifyAll()` (quando há mudança de estado):
```java
public synchronized String take() {
    while (empty) {
        try { wait(); } catch (InterruptedException e) {}
    }
    empty = true;
    notifyAll();
    return message;
}
```

## Implementação em Python
No Python, mapeamos esse comportamento idêntico através de um `threading.Condition()`, que envolve um lock e permite o uso de `wait()` e `notify_all()`:
```python
def take(self):
    with self._condition:
        while self._empty:
            self._condition.wait()
        self._empty = True
        self._condition.notify_all()
        return self._message
```

## Como Executar

### 1) Java
```bash
javac Drop.java Producer.java Consumer.java ProducerConsumerExample.java
java ProducerConsumerExample
```

### 2) Python
```bash
python main.py
```
