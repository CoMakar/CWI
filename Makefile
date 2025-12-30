include .build_info

pyi=pipenv run pyinstaller
version=v$(VERSION)

all: build pack

build:
	$(pyi) ${BUILD_NAME}.spec

pack:
	if not exist bin mkdir bin
	xcopy .\dist\${BUILD_NAME}.exe .\bin\${BUILD_NAME}\\ /Y
	if not exist .versions mkdir .versions
	tar -cvf "./.versions/${BUILD_NAME}_${version}_${BUILD_PLATFORM}.zip" -C "./bin/" "${BUILD_NAME}"

clean-build:
	if exist build rd /s /q build
	if exist dist rd /s /q dist

clean-setup:
	if exist setuptools-build rd /s /q setuptools-build
	if exist "src/${PKG_NAME}.egg-info" rd /s /q "src/${PKG_NAME}.egg-info"

.PHONY:	build