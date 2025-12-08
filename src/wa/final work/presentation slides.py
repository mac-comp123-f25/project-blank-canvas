import webview

url = "https://docs.google.com/presentation/d/e/2PACX-1vQd75hPcreBP8TqLUYqn6O8yXw9xBhIq7Lxb4tn6-SdLGO6RmpXGDRAq9ZwzHqGkqDV15f1oqvswM9v/pubembed?start=false&loop=false&delayms=3000"

webview.create_window("Slides", url)
webview.start()
