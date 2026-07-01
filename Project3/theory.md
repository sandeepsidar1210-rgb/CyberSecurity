# Project 3: Vulnerability Assessment Foundations & Risk Scoring

## 1. What is a Vulnerability?
* **Definition:** A weakness, flaw, or loophole in an information system, security procedure, internal control, or software code that can be exploited by a threat actor (cybercriminal) to gain unauthorized access to a network or system.
* **Vulnerability vs. Threat:** A vulnerability is the *weakness* (e.g., a broken window), while a threat is the *actor* or event that can exploit that weakness (e.g., a burglar).

## 2. Common Vulnerabilities and Exposures (CVE)
* **Definition:** CVE is an international, publicly available dictionary of known cybersecurity vulnerabilities. Every tracked vulnerability is assigned a unique tracking number (e.g., `CVE-2026-XXXX`).
* **Why it matters:** It provides a universal standard naming convention so that security engineers, vendors, and analysts worldwide are talking about the exact same system flaw.

## 3. CVSS v4.0 (Common Vulnerability Scoring System)
To prioritize patches, organizations use the CVSS scale to score flaws from **0.0 to 10.0**:
* **Low Risk (0.1 - 3.9):** Minor flaws that are extremely difficult to exploit or have almost zero impact.
* **Medium Risk (4.0 - 6.9):** Localized flaws that require specific conditions or local access to exploit.
* **High Risk (7.0 - 8.9):** Dangerous flaws that can allow privilege escalation or data leakage.
* **Critical Risk (9.0 - 10.0):** Severe bugs that allow remote attackers to fully control the system without any user interaction.

## 4. The Vulnerability Management Lifecycle
Security teams continuously run these 4 core phases to keep environments hardened:
1. **Identification (Discovery):** Running automated network scanners to probe systems and locate unpatched flaws.
2. **Analysis (Assessment):** Evaluating the discovered flaws and assigning them risk levels using CVE/CVSS frameworks.
3. **Remediation (Mitigation):** Applying software updates, security patches, or configuration changes to fix the loophole permanently.
4. **Verification:** Re-scanning the system to confirm that the security patches are working and the flaw is completely removed.