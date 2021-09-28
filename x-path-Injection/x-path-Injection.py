from flask import request, app
import xml.etree.ElementTree as ET
from lxml import etree

# flask app
@app.route('/user')
def non_conformant1():
    tree = ET.parse('users.xml')
    root = tree.getroot()
    username = request.args['username']
    query = "./users/user/[@name='"+username+"']/location"
    elmts = root.findall(query)
    return 'Location %s' % list(elmts)


@app.route('/someurl')
def non_conformant2():
    attribute_name = request.form.get("attribute_name")
    tree = ET.parse('users.xml')
    root = tree.getroot()
    attribute_value = root.findall(".//string[@name='{}']".format(attribute_name))


@app.route('/someurl')
def non_conformant3():
    document = ET.parse('data.xml')
    key = request.args.get("key")
    term = './string[@name=\'' + key + '\']'
    results = document.getroot().findall(term)


@app.route('/someurl')
def non_conformant4():
    path = 'data.xml'
    tree = ET.ElementTree()
    tree.parse(path)
    root = tree.getroot()
    voice = root.find("./voice/[@name='{}']".format(request.values.get("data")))


@app.route('/someurl')
def non_conformant5():
    root = ET.fromstring(repomd_content)
    primary_xml = request.values["data"]
    for md in primary_xml:
        if md is None:
            continue
        repodata = root.find(".//*[@type='{type}']".format(type=md.type_tag))


# Django
def non_conformant6(request):
    root = ET.fromstring(data)
    sensor_id = request.GET.get('sensor_id')
    calibration_element = root.find(".//chunk/sensors/sensor[@id='{}']/calibration".format(sensor_id))


def non_conformant7(request):
    station_id_to_fix = request.GET["id"]
    kmap = ET.parse(input_kmap_name)

    for fiducial in kmap.getroot().findall(".//*[@station='{}']".format(station_id_to_fix)):
        pass


def non_conformant8(request):
    root = ET.fromstring(data)
    para = request.POST["key"]
    root.findall('./string[@key=\'' + para + '\']')


def non_conformant9(request):
    tree = ET.parse('users.xml')
    root = tree.getroot()
    member_name, key_name, id = request.GET["member_name"], request.GET.get["key_name"], request.GET["id"]
    path = '/service/{0}[{1}="{2}"]'.format(member_name, key_name, id)
    return root.findall(path)

def non_conformant10():
    tree = ET.parse('users.xml')
    root = tree.getroot()
    section_id = request.values["id"]
    section_head = root.findall("//ul/li/"+section_id+"/")


# CONFORMANT CASES
# flask app
@app.route('/someurl')
def conformant1():
    parser = etree.XMLParser(resolve_entities=False)
    tree = etree.parse('users.xml', parser)
    root = tree.getroot()
    username = request.args['username']
    query = "/collection/users/user[@name = $paramname]/location/text()"
    elmts = root.xpath(query, paramname = username)
    return 'Location %s' % list(elmts)


@app.route('/someurl')
def conformant2(self):
    _SCALE_XML_NAME = 'Price Constraint Scaling Factor'
    tree = ET.parse(self._premia_config_local_path)
    all_scaling_factor_options = tree.findall('Options/Option[@Name="%s"]' % _SCALE_XML_NAME)


@app.route('/someurl')
def conformant3():
    section_id = request.args.get("username")
    section_head = menuroot.xpath("//ul[@id=$section]/li", section=section_id)


@app.route('/someurl')
def conformant4():
    styles = zin.read("styles.xml")
    root = etree.fromstring(styles)
    for el in root.xpath("//style:page-layout-properties",
                         namespaces=NAMESPACES):
        pass


@app.route('/someurl')
def conformant5(request):
    dom = etree.HTML(request.form["file_path"])
    tr_nodes = dom.xpath("//table[@id='customers']/tr")


# Django
def conformant6(request):
    parser = etree.XMLParser(resolve_entities=False)
    tree = etree.parse('users.xml', parser)
    root = tree.getroot()
    section_id = request.values["id"]
    section_head = root.xpath("//ul/li/")


def conformant7(xmlfile):
    root = xmlfile.getroot()
    for endpoint in root.findall('./endpointSet/endpoints/endpoint'):
        pass


def conformant8():
    tree = ET.parse('users.xml')
    root = tree.getroot()
    usage_col = root.find("./collection/[@label='Usage']")


def conformant9(tree):
    owner_id = tree.findtext(".//Owner//ID")