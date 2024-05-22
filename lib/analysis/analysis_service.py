from lib.analysis.analysis import Analysis
from lib.vulnerabilites.vulnerability import Vulnerability
from lib.gemini.gemini import Gemini


class AnalysisService:
    def __init__(self) -> None:
        self.gemini = Gemini()

    def generate_analysis_message(self, analysis: Analysis) -> str:
        prompt = """
            I have a list of vulnerabilities identified in Ethereum smart contracts by an analyzer tool. Each vulnerability is labeled with a specific name. I need a short analysis message that summarizes the implications and potential impact of each vulnerability. Here are the labels of the vulnerabilities:

        """

        for v in analysis.vulnerabilites:
            prompt += f"""
                - {v.name}
            """

        prompt += """

            Please provide a short analysis message that summarizes the potential impact of each vulnerability, without mentioning directly in bullet points, and finally give a resource that could help to fix the vulnerabilities.

            Expected format, no need to have an itroductory title. Give the content directly:
            [Analysis Message]
        """

        return self.gemini.prompt(prompt)

    def generate_vulnerability_desciption(self, vulnerability: Vulnerability) -> str:
        prompt = f"""
        I have a vulnerability identified in an Ethereum smart contract, labeled "{vulnerability.name}". I need a detailed description of this vulnerability, explaining what it is, how it occurs, and its potential impact.

        Please provide a detailed description for the following vulnerability:

        Vulnerability Name: {vulnerability.name}

        Expected format, no need to have an itroductory title. Give the content directly:
        [Description]
        """

        return self.gemini.prompt(prompt)

    def enhance_analysis(self, analysis: Analysis) -> Analysis:
        if len(analysis.vulnerabilites) > 0:
            analysis.message = self.generate_analysis_message(analysis)

        for v in analysis.vulnerabilites:
            v.desc = self.generate_vulnerability_desciption(v)

        return analysis

analysis_service = AnalysisService()
