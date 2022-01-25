<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:template match="/">
  <html>
  <xsl:for-each select="interfaces/interface">
    interface <xsl:value-of select="name"/>
      ip address <xsl:value-of select="ipv4addr"/>
  </xsl:for-each>
  </html>
</xsl:template>
</xsl:stylesheet>