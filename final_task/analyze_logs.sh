#!/bin/bash

# Генерация логов для тестирования
cat <<EOL > access.log
192.168.1.1 - - [28/Jul/2024:12:34:56 +0000] "GET /index.html HTTP/1.1" 200 1234
192.168.1.2 - - [28/Jul/2024:12:35:56 +0000] "POST /login HTTP/1.1" 200 567
192.168.1.3 - - [28/Jul/2024:12:36:56 +0000] "GET /home HTTP/1.1" 404 890
192.168.1.1 - - [28/Jul/2024:12:37:56 +0000] "GET /index.html HTTP/1.1" 200 1234
192.168.1.4 - - [28/Jul/2024:12:38:56 +0000] "GET /about HTTP/1.1" 200 432
192.168.1.2 - - [28/Jul/2024:12:39:56 +0000] "GET /index.html HTTP/1.1" 200 1234
EOL

# общее количество запросов
total_requests=$(wc -l < access.log)

# количество уникальных IP-адресов с использованием awk
unique_ips=$(awk '{print $1}' access.log | sort | uniq | wc -l)

# количество запросов по методам (GET, POST и т.д.) с использованием awk
methods=$(awk '{print $6}' access.log | tr -d '\"' | sort | uniq -c | awk '{print $2, $1}')

# Найти самый популярный URL с использованием awk
popular_url=$(awk '{print $7}' access.log | sort | uniq -c | sort -nr | head -1 | awk '{print $2}')

# Создать отчет в виде текстового файла
{
  echo "Отчет о логе веб-сервера"
  echo "========================="
  echo "Общее количество запросов: $total_requests"
  echo "Количество уникальных IP-адресов: $unique_ips"
  echo ""
  echo "Количество запросов по методам:"
  echo "$methods"
  echo ""
  echo "Самый популярный URL: $popular_url"
} > report.txt

# Выводим сообщение об успешном создании отчета
echo "Отчет сохранен в файл report.txt"
