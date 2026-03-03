APP_NAME = netmiko-app

# Build da imagem
build:
	docker build -t $(APP_NAME) .

# Deploy / inicia container interativo
deploy: build
	-docker stop $(APP_NAME)
	-docker rm $(APP_NAME)
	docker run -it --name $(APP_NAME) -v $(PWD)/scripts:/app/scripts $(APP_NAME)