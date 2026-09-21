# GFC Web Application Security & Ethical Hacking Lab

## Practical Web Application Penetration Testing Lab

This lab documents an authorized, hands-on security assessment of the GFC Financial Analysis Chatbot, a Flask-based financial analysis application deployed on Render.

## Lab identity

**Lab name:** GFC Web Application Security & Ethical Hacking Lab  
**Project:** GFC Financial Analysis Chatbot  
**Assessment type:** Authorized web application security assessment  
**Primary tool:** Burp Suite  
**Security platforms:** Kali Linux / Parrot OS  
**Target:** The project's own deployed application

## 🚀 Live Target

**Authorized application under assessment:**  
https://gfc-financial-analysis-chatbot.onrender.com/

This URL is the project's deployed application and is the only web target authorized by this lab documentation.

## Objectives

- Establish a professional penetration-testing methodology.
- Learn Burp Suite interception and HTTP analysis.
- Map the application's attack surface.
- Test input validation and error handling.
- Assess session and security configuration.
- Investigate common OWASP-style web vulnerabilities.
- Document reproducible findings.
- Fix identified weaknesses and perform verification testing.

## Scope

### In scope
- The GFC chatbot web application.
- Public HTTP/HTTPS endpoints belonging to the application.
- Application inputs and responses.
- Flask session behavior.
- Application security headers and configuration.
- Low-volume, controlled security tests.

### Out of scope
- Other Render customers or infrastructure.
- GitHub accounts, repositories or users unrelated to this project.
- DNS, network infrastructure or third-party services.
- Denial-of-service testing.
- Credential attacks against real users.
- Destructive exploitation.

## Methodology

1. Scope and rules of engagement
2. Reconnaissance and attack-surface mapping
3. Burp Suite proxy configuration
4. HTTP request/response analysis
5. Input-validation testing
6. Session and security-control testing
7. Injection and application-logic testing
8. Security-header/configuration review
9. Evidence collection
10. Risk assessment
11. Remediation
12. Retesting
13. Final security report

## Important lab rule

All testing must remain limited to the authorized GFC application. Keep automated requests low-volume, especially against the Render free instance.

## Portfolio outcome

This lab demonstrates practical knowledge of web application reconnaissance, HTTP fundamentals, Burp Suite, Flask security, input validation, session security, OWASP-style testing, vulnerability documentation, remediation and responsible penetration testing.
