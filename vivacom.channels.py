import re, requests

with open('vivacom.bg.channels.xml', 'w') as w:
  w.write('<channels>\n')
  for i in range(1, 25):
    url = "http://www.vivacom.bg/bg/tv/programa/?page=%s"
    url = url % i
    print "Requesting url %s " + url
    r = requests.get(url)
    matches = re.compile("li\s+title=\"(.*?)\">").findall(r.text)
    l = len(matches)
    print "Found %s channels " % l
    
    k = 1
    for m in matches:
      #print m
      site_id = "%s,%s,%s,%s" % (i, k, k + l, k + l + l)
      channel = '  <channel update="i" site="vivacom.bg" site_id="%s" xmltv_id="%s">%s</channel>' % (site_id, m, m)
      print channel
      w.write(channel.encode('utf-8') + '\n')
      k += 1

  w.write('</channels>')