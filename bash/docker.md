## This note shows the commands of docker

# 1. image related
# 1.1 list all images in the system
- `sudo docker images`

# 1.2 create a container from a specific image
- `sudo docker run -id --name container_name -v code_dir:mounted_dir image_name[:tag] or image_ID /bin/bash`
- `sudo docker create -id --name contrainer_name image_name[:tag] or image_ID`

# 1.3 remote or delete an image
- `sudo docker rmi image_name or image_ID`

# 1.4 pull or download an image from docker hub
- `sudo docker pull image_name[:tag]`

# 2. container related
# 2.1 get into a running container
- `sudo docker exec -it container_name or container_ID /bin/bash`
# 2.2 remove or delete a container
- `sudo docker container remove contrainer_name or container_ID`
# 2.3 list all the containers
- `sudo docker container list`
