# Фильтр алертов

Трек 01 «Агентные системы», упражнение «Отфильтруйте шум» — репетиция части, которая
ложится прямо на наш проект (агент, отсекающий шум в тревогах датчиков шахты).

## Что делает

Читает 8 событий из `events.json` (`info` / `warn` / `critical`), печатает только
`critical` и итоговую строку `summary: критичных N`.

Без агентов и тулов — обычный `filter` по полю `level`.

## Как запустить

```bash
cd track01_practice/02_alert_filter
python filter_alerts.py
```

## Что получилось

Из 8 событий (disk 90%, user login, cpu 40%, payment failed, heartbeat, db timeout,
cache miss, deploy ok) критичными оказались 3:

```
[CRITICAL] disk 90%
[CRITICAL] payment failed
[CRITICAL] db timeout
summary: критичных 3
```
