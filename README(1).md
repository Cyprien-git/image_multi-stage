``` bash 
docker build -t logos-app -f Dockerfile.nuitka . --no-cache
```

``` bash
docker run --rm -v $(pwd)/logos/data:/app/logos/data logos-app logos/data/RT.png
```