<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
	<xsl:output method="xml" encoding="UTF-8"/>
	<xsl:param name="conf"/>
	<xsl:template match="/dblp">
		<dblp>
			<xsl:for-each select="*">
				<xsl:if test="substring-after(@key,'conf/'+$conf)!=''">
					<xsl:copy-of select="."/>
				</xsl:if>
			</xsl:for-each>
		</dblp>
	</xsl:template>
</xsl:stylesheet>
