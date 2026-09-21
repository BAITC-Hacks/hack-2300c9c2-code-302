# Фильтр алертов

Трек 01 «Агентные системы», упражнение «Отфильтруйте шум» — репетиция части, которая
ложится прямо на наш проект (агент, отсекающий шум в тревогах датчиков шахты).

## Что делает

Читает 8 событий из `events.json` (`info` / `warn` / `critical`), печатает только
`critical` и итоговую строку `summary: критичных N`.

Без агентов и тулов — обычный `filter` по полю `level`.

## Как пользоваться

1. Запустите на заготовленных 8 событиях:
   ```bash
   cd track01_practice/02_alert_filter
   python filter_alerts.py
   ```
2. Чтобы проверить свои события — отредактируйте `events.json` (массив объектов
   `{"event": "...", "level": "info|warn|critical"}`) или укажите другой файл:
   ```bash
   python filter_alerts.py my_events.json
   ```

Скрипт сам печатает вывод в UTF-8 (`sys.stdout.reconfigure`), поэтому кириллица в
`summary` корректно отображается в любом терминале без дополнительных переменных
окружения. Уровень `level` сравнивается без учёта регистра (`CRITICAL` == `critical`).

## Что получилось

Из 8 событий (disk 90%, user login, cpu 40%, payment failed, heartbeat, db timeout,
cache miss, deploy ok) критичными оказались 3:

```
[CRITICAL] disk 90%
[CRITICAL] payment failed
[CRITICAL] db timeout
summary: критичных 3
```
