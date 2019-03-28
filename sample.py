import requests

def run(url):
    print("downloading...")
    response = requests.get(url)
    assert response.status_code == 200, "[ERROR] states_code is {}".format(response.status_code)

    contentType = response.headers['Content-Type']
    contentDisposition = response.headers['Content-Disposition']
    ATTRIBUTE = 'filename='
    fileName = contentDisposition[contentDisposition.find(
        ATTRIBUTE) + len(ATTRIBUTE):]
    fileName = fileName.replace('"', '')

    saveFilePath = fileName
    with open(saveFilePath, 'wb') as saveFile:
        saveFile.write(response.content)
    print("successfully saved {}".format(saveFilePath))

if __name__ == '__main__':
    # urlには先ほど取得したurl
    url = "https:\/\/signate-prd.s3.ap-northeast-1.amazonaws.com\/datasets\/149\/master.tsv?X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIOPRBJGKMEQPRJUA%2F20190328%2Fap-northeast-1%2Fs3%2Faws4_request&X-Amz-Date=20190328T075216Z&X-Amz-SignedHeaders=host&X-Amz-Expires=600&X-Amz-Signature=8d9b0ff27a22e379ffde9ea669cf85a67f6282332bd99efd775e5a10cc17cbfe"
    url = url.replace("\\", "")
    run(url)
