#!/usr/bin/env python3
"""
███████╗ ██████╗  ██████╗██╗ █████╗ ██╗     ██╗███╗   ██╗████████╗███████╗██╗     ██╗      █████╗ ██╗  ██╗
██╔════╝██╔═══██╗██╔════╝██║██╔══██╗██║     ██║████╗  ██║╚══██╔══╝██╔════╝██║     ██║     ██╔══██╗╚██╗██╔╝
███████╗██║   ██║██║     ██║███████║██║     ██║██╔██╗ ██║   ██║   █████╗  ██║     ██║     ███████║ ╚███╔╝ 
╚════██║██║   ██║██║     ██║██╔══██║██║     ██║██║╚██╗██║   ██║   ██╔══╝  ██║     ██║     ██╔══██║ ██╔██╗ 
███████║╚██████╔╝╚██████╗██║██║  ██║███████╗██║██║ ╚████║   ██║   ███████╗███████╗███████╗██║  ██║██╔╝ ██╗
╚══════╝ ╚═════╝  ╚═════╝╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝

⚡ SocialIntellax - Ethical OSINT & Threat Intelligence Framework ⚡
👤 Author: Inayat Hussain Chohan (Pakistani Cybersecurity Researcher & AI Practitioner)
🔍 Purpose: Comprehensive OSINT Intelligence Gathering Tool
"""

import requests
import re
import json
import os
import sys
import time
import webbrowser
from datetime import datetime
from urllib.parse import quote, urlparse
from colorama import init, Fore, Back, Style
from bs4 import BeautifulSoup
from tabulate import tabulate
import base64

# Initialize colorama for cross-platform colored output
init(autoreset=True)

class SocialIntellax:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        self.output_dir = "socialintellax_output"
        os.makedirs(self.output_dir, exist_ok=True)
        
    def print_banner(self):
        banner = f"""
{Fore.CYAN}███████╗ ██████╗  ██████╗██╗ █████╗ ██╗     ██╗███╗   ██╗████████╗███████╗██╗     ██╗      █████╗ ██╗  ██╗
██╔════╝██╔═══██╗██╔════╝██║██╔══██╗██║     ██║████╗  ██║╚══██╔══╝██╔════╝██║     ██║     ██╔══██╗╚██╗██╔╝
███████╗██║   ██║██║     ██║███████║██║     ██║██╔██╗ ██║   ██║   █████╗  ██║     ██║     ███████║ ╚███╔╝ 
╚════██║██║   ██║██║     ██║██╔══██║██║     ██║██║╚██╗██║   ██║   ██╔══╝  ██║     ██║     ██╔══██║ ██╔██╗ 
███████║╚██████╔╝╚██████╗██║██║  ██║███████╗██║██║ ╚████║   ██║   ███████╗███████╗███████╗██║  ██║██╔╝ ██╗
╚══════╝ ╚═════╝  ╚═════╝╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝{Style.RESET_ALL}

{Fore.YELLOW}⚡ SocialIntellax - Ethical OSINT & Threat Intelligence Framework ⚡{Style.RESET_ALL}
{Fore.GREEN}👤 Author: Inayat Hussain Chohan (Pakistani Cybersecurity Researcher & AI Practitioner){Style.RESET_ALL}
{Fore.BLUE}🔍 Purpose: Comprehensive OSINT Intelligence Gathering Tool{Style.RESET_ALL}
{Fore.RED}⚠️  Warning: For Educational and Ethical Use Only!{Style.RESET_ALL}
"""
        print(banner)

    def print_success(self, message):
        print(f"{Fore.GREEN}[✓] {message}{Style.RESET_ALL}")

    def print_info(self, message):
        print(f"{Fore.CYAN}[ℹ] {message}{Style.RESET_ALL}")

    def print_warning(self, message):
        print(f"{Fore.YELLOW}[⚠] {message}{Style.RESET_ALL}")

    def print_error(self, message):
        print(f"{Fore.RED}[✗] {message}{Style.RESET_ALL}")

    def save_output(self, data, module_name, target):
        """Save output to file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.output_dir}/{module_name}_{target}_{timestamp}.txt"
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"SocialIntellax Output\n")
                f.write(f"Module: {module_name}\n")
                f.write(f"Target: {target}\n")
                f.write(f"Timestamp: {datetime.now()}\n")
                f.write("=" * 50 + "\n\n")
                f.write(data)
            self.print_success(f"Output saved to: {filename}")
        except Exception as e:
            self.print_error(f"Error saving output: {e}")

    def google_search(self, query, num_results=10):
        """Perform Google search with dorks"""
        try:
            search_url = f"https://www.google.com/search?q={quote(query)}&num={num_results}"
            response = self.session.get(search_url, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            results = []
            for result in soup.find_all('div', class_='g'):
                link_elem = result.find('a')
                if link_elem and link_elem.get('href'):
                    url = link_elem.get('href')
                    if url.startswith('/url?q='):
                        url = url.replace('/url?q=', '').split('&')[0]
                    title_elem = result.find('h3')
                    title = title_elem.get_text() if title_elem else "No title"
                    results.append({'url': url, 'title': title})
            
            return results
        except Exception as e:
            self.print_error(f"Google search error: {e}")
            return []

    def instagram_osint(self, username):
        """Instagram OSINT Module"""
        self.print_info(f"Starting Instagram OSINT for: {username}")
        
        try:
            # Check if profile exists
            url = f"https://www.instagram.com/{username}/"
            response = self.session.get(url, timeout=10)
            
            results = []
            if response.status_code == 200:
                self.print_success(f"Instagram profile found: {url}")
                results.append(f"Profile URL: {url}")
                
                # Try to extract basic info from meta tags
                soup = BeautifulSoup(response.content, 'html.parser')
                meta_desc = soup.find('meta', attrs={'name': 'description'})
                if meta_desc:
                    results.append(f"Description: {meta_desc.get('content', 'N/A')}")
                
                # Look for JSON data
                scripts = soup.find_all('script', type='application/ld+json')
                for script in scripts:
                    try:
                        data = json.loads(script.string)
                        if 'name' in data:
                            results.append(f"Name: {data.get('name', 'N/A')}")
                        break
                    except:
                        continue
            else:
                self.print_warning(f"Instagram profile not found or private: {username}")
                results.append(f"Profile not found or private: {username}")
            
            # Google dorks for additional info
            dorks = [
                f'site:instagram.com "{username}"',
                f'"{username}" site:instagram.com',
            ]
            
            for dork in dorks:
                google_results = self.google_search(dork, 5)
                for result in google_results:
                    results.append(f"Google Result: {result['title']} - {result['url']}")
            
            output = "\n".join(results)
            self.save_output(output, "instagram", username)
            self.print_success("Instagram OSINT completed")
            
        except Exception as e:
            self.print_error(f"Instagram OSINT error: {e}")

    def facebook_osint(self, username):
        """Facebook OSINT Module"""
        self.print_info(f"Starting Facebook OSINT for: {username}")
        
        try:
            results = []
            fb_url = f"https://www.facebook.com/{username}"
            
            response = self.session.get(fb_url, timeout=10)
            if "content=\"0; URL=" in response.text or "Page Not Found" in response.text:
                self.print_warning(f"Facebook profile not found: {username}")
                results.append(f"Profile not found: {username}")
            else:
                self.print_success(f"Possible Facebook profile: {fb_url}")
                results.append(f"Profile URL: {fb_url}")
            
            # Google dorks
            dorks = [
                f'site:facebook.com "{username}"',
                f'site:facebook.com/people "{username}"',
            ]
            
            for dork in dorks:
                google_results = self.google_search(dork, 5)
                for result in google_results:
                    results.append(f"Google Result: {result['title']} - {result['url']}")
            
            output = "\n".join(results)
            self.save_output(output, "facebook", username)
            self.print_success("Facebook OSINT completed")
            
        except Exception as e:
            self.print_error(f"Facebook OSINT error: {e}")

    def linkedin_osint(self, target):
        """LinkedIn OSINT Module"""
        self.print_info(f"Starting LinkedIn OSINT for: {target}")
        
        try:
            results = []
            
            # Check direct profile
            profile_url = f"https://www.linkedin.com/in/{target}"
            response = self.session.get(profile_url, timeout=10)
            
            if response.status_code == 200:
                self.print_success(f"LinkedIn profile found: {profile_url}")
                results.append(f"Profile URL: {profile_url}")
            else:
                self.print_warning(f"LinkedIn profile not found: {target}")
            
            # Google dorks for LinkedIn
            dorks = [
                f'site:linkedin.com/in "{target}"',
                f'site:linkedin.com "{target}"',
                f'site:linkedin.com/in/ AND company "{target}"',
                f'site:linkedin.com/in/ AND location "{target}"',
            ]
            
            for dork in dorks:
                self.print_info(f"Searching: {dork}")
                google_results = self.google_search(dork, 5)
                for result in google_results:
                    results.append(f"LinkedIn Result: {result['title']} - {result['url']}")
            
            output = "\n".join(results)
            self.save_output(output, "linkedin", target)
            self.print_success("LinkedIn OSINT completed")
            
        except Exception as e:
            self.print_error(f"LinkedIn OSINT error: {e}")

    def twitter_osint(self, username):
        """Twitter/X OSINT Module"""
        self.print_info(f"Starting Twitter/X OSINT for: {username}")
        
        try:
            results = []
            
            # Check profile existence
            twitter_urls = [
                f"https://twitter.com/{username}",
                f"https://x.com/{username}"
            ]
            
            for url in twitter_urls:
                try:
                    response = self.session.get(url, timeout=10)
                    if response.status_code == 200:
                        self.print_success(f"Twitter profile found: {url}")
                        results.append(f"Profile URL: {url}")
                        break
                except:
                    continue
            
            # Google dorks
            dorks = [
                f'site:twitter.com "{username}"',
                f'site:x.com "{username}"',
                f'"@{username}" site:twitter.com',
            ]
            
            for dork in dorks:
                google_results = self.google_search(dork, 5)
                for result in google_results:
                    results.append(f"Twitter Result: {result['title']} - {result['url']}")
            
            output = "\n".join(results)
            self.save_output(output, "twitter", username)
            self.print_success("Twitter/X OSINT completed")
            
        except Exception as e:
            self.print_error(f"Twitter OSINT error: {e}")

    def youtube_osint(self, target):
        """YouTube OSINT Module"""
        self.print_info(f"Starting YouTube OSINT for: {target}")
        
        try:
            results = []
            
            # Check channel existence
            channel_formats = [
                f"https://www.youtube.com/c/{target}",
                f"https://www.youtube.com/@{target}",
                f"https://www.youtube.com/user/{target}"
            ]
            
            for url in channel_formats:
                try:
                    response = self.session.get(url, timeout=10)
                    if response.status_code == 200 and "channel" in response.text.lower():
                        self.print_success(f"YouTube channel found: {url}")
                        results.append(f"Channel URL: {url}")
                        break
                except:
                    continue
            
            # Google dorks
            dorks = [
                f'site:youtube.com "{target}"',
                f'site:youtube.com/c/{target}',
                f'site:youtube.com/@{target}',
            ]
            
            for dork in dorks:
                google_results = self.google_search(dork, 5)
                for result in google_results:
                    results.append(f"YouTube Result: {result['title']} - {result['url']}")
            
            output = "\n".join(results)
            self.save_output(output, "youtube", target)
            self.print_success("YouTube OSINT completed")
            
        except Exception as e:
            self.print_error(f"YouTube OSINT error: {e}")

    def github_osint(self, username):
        """GitHub OSINT Module"""
        self.print_info(f"Starting GitHub OSINT for: {username}")
        
        try:
            results = []
            
            # Check GitHub profile
            github_url = f"https://github.com/{username}"
            response = self.session.get(github_url, timeout=10)
            
            if response.status_code == 200:
                self.print_success(f"GitHub profile found: {github_url}")
                results.append(f"Profile URL: {github_url}")
                
                # Try to get basic info
                soup = BeautifulSoup(response.content, 'html.parser')
                name_elem = soup.find('span', {'class': 'p-name'})
                if name_elem:
                    results.append(f"Name: {name_elem.get_text().strip()}")
                
                bio_elem = soup.find('div', {'class': 'p-note'})
                if bio_elem:
                    results.append(f"Bio: {bio_elem.get_text().strip()}")
            
            # GitHub dorks for sensitive information
            dorks = [
                f'site:github.com "{username}"',
                f'site:github.com "{username}" password',
                f'site:github.com "{username}" api_key',
                f'site:github.com "{username}" secret',
            ]
            
            for dork in dorks:
                google_results = self.google_search(dork, 5)
                for result in google_results:
                    results.append(f"GitHub Result: {result['title']} - {result['url']}")
            
            output = "\n".join(results)
            self.save_output(output, "github", username)
            self.print_success("GitHub OSINT completed")
            
        except Exception as e:
            self.print_error(f"GitHub OSINT error: {e}")

    def google_dork_search(self, target):
        """Google Dork Search Module"""
        self.print_info(f"Starting Google Dork Search for: {target}")
        
        dorks = {
            "Login Pages": f'inurl:login site:{target}',
            "Exposed Docs": f'site:{target} filetype:pdf OR filetype:xls OR filetype:docx',
            "Directory Listings": f'intitle:"index of" site:{target}',
            "Sensitive Configs": f'site:{target} ext:env OR ext:xml OR ext:conf OR ext:ini',
            "Emails & Contacts": f'site:{target} "@{target}"',
            "GitHub Leaks": f'site:github.com "{target}"',
            "LinkedIn Profiles": f'site:linkedin.com/in "{target}"',
            "Exposed Passwords": f'site:{target} intext:password OR passwd OR pwd',
            "Social Media": f'"{target}" site:facebook.com OR site:twitter.com OR site:instagram.com',
            "Pastebin Leaks": f'site:pastebin.com "{target}"',
        }
        
        results = []
        for category, dork in dorks.items():
            self.print_info(f"Searching: {category}")
            google_results = self.google_search(dork, 5)
            
            if google_results:
                results.append(f"\n--- {category} ---")
                for result in google_results:
                    results.append(f"{result['title']} - {result['url']}")
            else:
                results.append(f"\n--- {category} ---")
                results.append("No results found")
        
        output = "\n".join(results)
        self.save_output(output, "google_dorks", target)
        self.print_success("Google Dork Search completed")

    def email_lookup(self, email):
        """Email Lookup Module"""
        self.print_info(f"Starting Email Lookup for: {email}")
        
        try:
            results = []
            
            # Extract domain if full email provided
            if "@" in email:
                domain = email.split("@")[1]
                results.append(f"Email: {email}")
                results.append(f"Domain: {domain}")
            else:
                domain = email
                results.append(f"Domain: {domain}")
            
            # Google dorks for email/domain
            dorks = [
                f'"{email}"' if "@" in email else f'"@{domain}"',
                f'"{email}" OR "{domain}" site:pastebin.com',
                f'"{email}" OR "{domain}" filetype:pdf',
                f'"{email}" OR "{domain}" site:github.com',
            ]
            
            for dork in dorks:
                google_results = self.google_search(dork, 5)
                for result in google_results:
                    results.append(f"Found: {result['title']} - {result['url']}")
            
            # Generate possible email formats if name provided
            name = input("Enter full name for email format generation (optional): ").strip()
            if name and domain:
                formats = self.generate_email_formats(name, domain)
                results.append("\nPossible Email Formats:")
                results.extend(formats)
            
            output = "\n".join(results)
            self.save_output(output, "email_lookup", email)
            self.print_success("Email Lookup completed")
            
        except Exception as e:
            self.print_error(f"Email Lookup error: {e}")

    def generate_email_formats(self, name, domain):
        """Generate possible email formats"""
        name_parts = name.lower().split()
        if len(name_parts) < 2:
            return [f"{name.lower()}@{domain}"]
        
        first, last = name_parts[0], name_parts[-1]
        formats = [
            f"{first}@{domain}",
            f"{last}@{domain}",
            f"{first}.{last}@{domain}",
            f"{first}_{last}@{domain}",
            f"{first}{last}@{domain}",
            f"{first[0]}{last}@{domain}",
            f"{first}{last[0]}@{domain}",
        ]
        return formats

    def username_reverse_search(self, username):
        """Username Reverse Search Module"""
        self.print_info(f"Starting Username Reverse Search for: {username}")
        
        platforms = {
            "GitHub": f"https://github.com/{username}",
            "Reddit": f"https://www.reddit.com/user/{username}",
            "Twitter": f"https://twitter.com/{username}",
            "Instagram": f"https://instagram.com/{username}",
            "LinkedIn": f"https://www.linkedin.com/in/{username}",
            "YouTube": f"https://www.youtube.com/@{username}",
            "TikTok": f"https://www.tiktok.com/@{username}",
            "Pastebin": f"https://pastebin.com/u/{username}",
        }
        
        results = []
        for platform, url in platforms.items():
            try:
                response = self.session.get(url, timeout=5)
                if response.status_code == 200:
                    self.print_success(f"Found on {platform}: {url}")
                    results.append(f"✓ {platform}: {url}")
                else:
                    results.append(f"✗ {platform}: Not found")
            except:
                results.append(f"? {platform}: Error checking")
        
        output = "\n".join(results)
        self.save_output(output, "username_search", username)
        self.print_success("Username Reverse Search completed")

    def pastebin_scraper(self, keyword):
        """Pastebin Scraper Module"""
        self.print_info(f"Starting Pastebin Search for: {keyword}")
        
        try:
            # Use Google to search Pastebin
            dork = f'site:pastebin.com "{keyword}"'
            results = []
            
            google_results = self.google_search(dork, 10)
            for result in google_results:
                results.append(f"Pastebin Result: {result['title']} - {result['url']}")
                
                # Try to fetch content and look for sensitive data
                try:
                    paste_response = self.session.get(result['url'], timeout=5)
                    if paste_response.status_code == 200:
                        content = paste_response.text
                        
                        # Look for emails
                        emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', content)
                        if emails:
                            results.append(f"  Emails found: {', '.join(set(emails))}")
                        
                        # Look for potential passwords
                        if any(word in content.lower() for word in ['password', 'passwd', 'pwd']):
                            results.append(f"  Potential password content detected")
                            
                except:
                    continue
            
            if not results:
                results.append("No Pastebin results found")
            
            output = "\n".join(results)
            self.save_output(output, "pastebin", keyword)
            self.print_success("Pastebin Search completed")
            
        except Exception as e:
            self.print_error(f"Pastebin Search error: {e}")

    def darkweb_intel(self, target):
        """Dark Web Intelligence Simulation"""
        self.print_info(f"Starting Dark Web Intelligence Search for: {target}")
        
        # This is a simulation - real dark web searching requires Tor
        results = [
            "=== DARK WEB INTELLIGENCE SIMULATION ===",
            f"Target: {target}",
            "",
            "Note: This is a simulation. Real dark web searching requires:",
            "- Tor Browser",
            "- Proper OpSec",
            "- Legal considerations",
            "",
            "Simulated Dark Web Sources:",
            "- Ahmia.fi (Surface web gateway)",
            "- DuckDuckGo Onion",
            "- Various .onion forums",
            "",
            f"Simulated findings for '{target}':",
            "- No direct matches found (simulation)",
            "- Recommend manual verification with proper tools",
            "",
            "Google Dorks for Public Leak Detection:",
        ]
        
        # Use public leak detection dorks
        dorks = [
            f'site:pastebin.com "{target}"',
            f'site:throwbin.io "{target}"',
            f'"{target}" "leak" OR "dump" OR "breach"',
            f'"{target}" site:raidforums.com',
        ]
        
        for dork in dorks:
            results.append(f"Dork: {dork}")
            google_results = self.google_search(dork, 3)
            for result in google_results:
                results.append(f"  Result: {result['url']}")
        
        output = "\n".join(results)
        self.save_output(output, "darkweb", target)
        self.print_success("Dark Web Intelligence simulation completed")

    def geoip_lookup(self, target):
        """GeoIP Lookup Module"""
        self.print_info(f"Starting GeoIP Lookup for: {target}")
        
        try:
            # Use free IP geolocation API
            url = f"http://ip-api.com/json/{target}?fields=status,message,country,regionName,city,zip,lat,lon,isp,org,as"
            response = self.session.get(url, timeout=10)
            data = response.json()
            
            if data.get("status") == "fail":
                self.print_error(f"GeoIP lookup failed: {data.get('message', 'Unknown error')}")
                return
            
            # Create table data
            table_data = [
                ["Field", "Value"],
                ["IP Address", target],
                ["Country", data.get("country", "N/A")],
                ["Region", data.get("regionName", "N/A")],
                ["City", data.get("city", "N/A")],
                ["ZIP Code", data.get("zip", "N/A")],
                ["Latitude", data.get("lat", "N/A")],
                ["Longitude", data.get("lon", "N/A")],
                ["ISP", data.get("isp", "N/A")],
                ["Organization", data.get("org", "N/A")],
                ["AS", data.get("as", "N/A")],
            ]
            
            # Print table
            print(tabulate(table_data[1:], headers=table_data[0], tablefmt="grid"))
            
            # Create Google Maps link
            if data.get("lat") and data.get("lon"):
                maps_url = f"https://www.google.com/maps?q={data['lat']},{data['lon']}"
                self.print_info(f"Google Maps: {maps_url}")
                table_data.append(["Google Maps", maps_url])
            
            # Save output
            output = tabulate(table_data[1:], headers=table_data[0], tablefmt="plain")
            self.save_output(output, "geoip", target)
            self.print_success("GeoIP Lookup completed")
            
        except Exception as e:
            self.print_error(f"GeoIP Lookup error: {e}")

    def metadata_extractor(self, file_path):
        """Metadata Extractor Module (Simulation)"""
        self.print_info(f"Starting Metadata Extraction for: {file_path}")
        
        if not os.path.exists(file_path):
            self.print_error(f"File not found: {file_path}")
            return
        
        results = [
            f"=== METADATA EXTRACTION SIMULATION ===",
            f"File: {file_path}",
            f"File Size: {os.path.getsize(file_path)} bytes",
            f"Created: {time.ctime(os.path.getctime(file_path))}",
            f"Modified: {time.ctime(os.path.getmtime(file_path))}",
            "",
            "Note: Full metadata extraction requires specialized libraries:",
            "- exifread (for images)",
            "- PyPDF2 (for PDFs)",
            "- python-docx (for Word docs)",
            "",
            "Simulated metadata that could be extracted:",
            "- GPS coordinates (if image)",
            "- Camera make/model (if image)",
            "- Author information (if document)",
            "- Creation software (if document)",
        ]
        
        output = "\n".join(results)
        self.save_output(output, "metadata", os.path.basename(file_path))
        self.print_success("Metadata Extraction completed")

    def reverse_image_search(self, image_path):
        """Reverse Image Search Module"""
        self.print_info(f"Starting Reverse Image Search for: {image_path}")
        
        if not os.path.exists(image_path):
            self.print_error(f"Image file not found: {image_path}")
            return
        
        results = [
            "=== REVERSE IMAGE SEARCH ===",
            f"Image: {image_path}",
            "",
            "Opening reverse image search engines in browser:",
        ]
        
        # Google Images
        google_url = "https://images.google.com"
        self.print_info(f"Opening Google Images: {google_url}")
        webbrowser.open(google_url)
        results.append(f"Google Images: {google_url}")
        
        # Yandex Images
        yandex_url = "https://yandex.com/images/"
        self.print_info(f"Opening Yandex Images: {yandex_url}")
        webbrowser.open(yandex_url)
        results.append(f"Yandex Images: {yandex_url}")
        
        # TinEye
        tineye_url = "https://tineye.com/"
        self.print_info(f"Opening TinEye: {tineye_url}")
        webbrowser.open(tineye_url)
        results.append(f"TinEye: {tineye_url}")
        
        results.append("")
        results.append("Please manually upload the image to these services for reverse search.")
        
        output = "\n".join(results)
        self.save_output(output, "reverse_image", os.path.basename(image_path))
        self.print_success("Reverse Image Search URLs opened in browser")

    def phishing_url_check(self, url):
        """Phishing URL Check Module"""
        self.print_info(f"Starting Phishing URL Check for: {url}")
        
        try:
            results = [
                "=== PHISHING URL ANALYSIS ===",
                f"URL: {url}",
                ""
            ]
            
            # Parse URL
            parsed = urlparse(url)
            results.append(f"Domain: {parsed.netloc}")
            results.append(f"Scheme: {parsed.scheme}")
            results.append(f"Path: {parsed.path}")
            results.append("")
            
            # Basic checks
            suspicious_indicators = []
            
            # Check for HTTPS
            if parsed.scheme != 'https':
                suspicious_indicators.append("❌ Not using HTTPS")
            else:
                results.append("✅ Using HTTPS")
            
            # Check for suspicious TLDs
            suspicious_tlds = ['.tk', '.ml', '.ga', '.cf', '.click', '.download']
            if any(tld in parsed.netloc for tld in suspicious_tlds):
                suspicious_indicators.append("❌ Suspicious TLD detected")
            
            # Check for URL shorteners
            shorteners = ['bit.ly', 'tinyurl.com', 'goo.gl', 't.co', 'ow.ly']
            if any(shortener in parsed.netloc for shortener in shorteners):
                suspicious_indicators.append("⚠️ URL shortener detected")
            
            # Check for typosquatting patterns
            legitimate_domains = ['google.com', 'facebook.com', 'amazon.com', 'microsoft.com', 'apple.com']
            for domain in legitimate_domains:
                if domain.replace('.', '') in parsed.netloc and domain not in parsed.netloc:
                    suspicious_indicators.append(f"❌ Possible typosquatting of {domain}")
            
            # Check domain reputation using Google Safe Browsing (simulation)
            results.append("Google Safe Browsing Check:")
            results.append("Note: This would require API key for real implementation")
            results.append("Simulated result: No threats detected")
            results.append("")
            
            # Display suspicious indicators
            if suspicious_indicators:
                results.append("⚠️ SUSPICIOUS INDICATORS FOUND:")
                results.extend(suspicious_indicators)
            else:
                results.append("✅ No obvious suspicious indicators found")
            
            results.append("")
            results.append("Recommendations:")
            results.append("- Verify sender legitimacy")
            results.append("- Check spelling and grammar")
            results.append("- Look for urgency tactics")
            results.append("- When in doubt, don't click")
            
            output = "\n".join(results)
            self.save_output(output, "phishing_check", parsed.netloc)
            self.print_success("Phishing URL Check completed")
            
        except Exception as e:
            self.print_error(f"Phishing URL Check error: {e}")

    def mutuals_detector(self, username1, username2=None):
        """Mutuals Detector Module"""
        if not username2:
            username2 = input("Enter second username to compare: ").strip()
        
        self.print_info(f"Starting Mutuals Detection: {username1} vs {username2}")
        
        results = [
            "=== MUTUALS DETECTION (EXPERIMENTAL) ===",
            f"User 1: {username1}",
            f"User 2: {username2}",
            "",
            "Searching for common appearances..."
        ]
        
        # Search for both usernames appearing together
        platforms = ["facebook", "instagram", "linkedin", "github", "twitter", "reddit"]
        
        for platform in platforms:
            dork = f'"{username1}" AND "{username2}" site:{platform}.com'
            self.print_info(f"Checking {platform}...")
            
            google_results = self.google_search(dork, 3)
            if google_results:
                results.append(f"\n{platform.upper()} - Possible connections:")
                for result in google_results:
                    results.append(f"  {result['title']} - {result['url']}")
            else:
                results.append(f"\n{platform.upper()} - No connections found")
        
        output = "\n".join(results)
        self.save_output(output, "mutuals", f"{username1}_vs_{username2}")
        self.print_success("Mutuals Detection completed")

    def reddit_osint(self, username):
        """Reddit OSINT Module"""
        self.print_info(f"Starting Reddit OSINT for: {username}")
        
        try:
            results = []
            
            # Check Reddit profile
            reddit_url = f"https://www.reddit.com/user/{username}"
            response = self.session.get(reddit_url, timeout=10)
            
            if response.status_code == 200:
                self.print_success(f"Reddit profile found: {reddit_url}")
                results.append(f"Profile URL: {reddit_url}")
            else:
                self.print_warning(f"Reddit profile not found: {username}")
            
            # Google dorks for Reddit
            dorks = [
                f'site:reddit.com "{username}"',
                f'site:reddit.com inurl:user "{username}"',
                f'site:reddit.com "{username}" password',
                f'site:reddit.com "{username}" email',
            ]
            
            for dork in dorks:
                google_results = self.google_search(dork, 5)
                for result in google_results:
                    results.append(f"Reddit Result: {result['title']} - {result['url']}")
            
            output = "\n".join(results)
            self.save_output(output, "reddit", username)
            self.print_success("Reddit OSINT completed")
            
        except Exception as e:
            self.print_error(f"Reddit OSINT error: {e}")

    def archive_lookup(self, target):
        """Archive.org Lookup Module"""
        self.print_info(f"Starting Archive.org Lookup for: {target}")
        
        try:
            # Use Wayback Machine API
            api_url = f"http://web.archive.org/cdx/search/cdx?url={target}/*&output=json&collapse=urlkey"
            response = self.session.get(api_url, timeout=10)
            data = response.json()
            
            results = [
                "=== WAYBACK MACHINE RESULTS ===",
                f"Target: {target}",
                ""
            ]
            
            if len(data) > 1:
                self.print_success(f"Found {len(data)-1} archived snapshots")
                results.append(f"Total snapshots found: {len(data)-1}")
                results.append("\nRecent snapshots:")
                
                # Show first 10 snapshots
                for entry in data[1:11]:
                    timestamp = entry[1]
                    url = entry[2]
                    archived_url = f"http://web.archive.org/web/{timestamp}/{url}"
                    results.append(f"  {timestamp}: {archived_url}")
                    
            else:
                self.print_warning("No archived versions found")
                results.append("No archived versions found")
            
            output = "\n".join(results)
            self.save_output(output, "archive", target)
            self.print_success("Archive.org Lookup completed")
            
        except Exception as e:
            self.print_error(f"Archive.org Lookup error: {e}")

    def company_dorks(self, company):
        """Company Employee Dorking Module"""
        self.print_info(f"Starting Company Dorking for: {company}")
        
        dorks = [
            f'site:linkedin.com/in AND "@{company}"',
            f'site:linkedin.com/employees AND "@{company}"',
            f'site:pastebin.com "{company}"',
            f'site:github.com "@{company}"',
            f'"{company}" ext:pdf | ext:doc | ext:xls',
            f'"{company}" intitle:"index of"',
            f'"{company}" AND ("password" OR "credential" OR "username")',
            f'site:careers.{company} OR site:jobs.{company}',
            f'inurl:admin "{company}"',
        ]
        
        results = [
            f"=== COMPANY DORKING RESULTS ===",
            f"Company: {company}",
            ""
        ]
        
        for dork in dorks:
            self.print_info(f"Searching: {dork}")
            results.append(f"\nDork: {dork}")
            
            google_results = self.google_search(dork, 5)
            if google_results:
                for result in google_results:
                    results.append(f"  {result['title']} - {result['url']}")
            else:
                results.append("  No results found")
        
        output = "\n".join(results)
        self.save_output(output, "company_dorks", company)
        self.print_success("Company Dorking completed")

    def discord_lookup(self, target):
        """Discord Lookup Module (Simulation)"""
        self.print_info(f"Starting Discord Lookup for: {target}")
        
        results = [
            "=== DISCORD LOOKUP SIMULATION ===",
            f"Target: {target}",
            "",
            "Searching for Discord mentions..."
        ]
        
        # Google dorks for Discord
        dorks = [
            f'site:discord.com/invite "{target}"',
            f'site:discord.gg "{target}"',
            f'"{target}" discord server',
            f'"{target}" discord.gg',
        ]
        
        for dork in dorks:
            google_results = self.google_search(dork, 5)
            if google_results:
                results.append(f"\nFound Discord references:")
                for result in google_results:
                    results.append(f"  {result['title']} - {result['url']}")
            else:
                results.append(f"\nNo Discord references found for: {dork}")
        
        output = "\n".join(results)
        self.save_output(output, "discord", target)
        self.print_success("Discord Lookup completed")

    def show_menu(self):
        """Display main menu"""
        menu = f"""
{Fore.CYAN}╔══════════════════════════════════════════════════════════════╗
║                    SOCIALINTELLAX MODULES                     ║
╠══════════════════════════════════════════════════════════════╣{Style.RESET_ALL}
{Fore.GREEN}║  1.  Instagram OSINT      │  11. Dark Web Intel (Sim)      ║
║  2.  Facebook OSINT       │  12. GeoIP Lookup               ║
║  3.  LinkedIn OSINT       │  13. Metadata Extractor         ║
║  4.  Twitter/X OSINT      │  14. Reverse Image Search       ║
║  5.  YouTube OSINT        │  15. Phishing URL Check         ║
║  6.  GitHub OSINT         │  16. Mutuals Detector           ║
║  7.  Google Dork Search   │  17. Reddit OSINT               ║
║  8.  Email Lookup         │  18. Archive.org Lookup         ║
║  9.  Username Search      │  19. Company Dorking            ║
║  10. Pastebin Scraper     │  20. Discord Lookup             ║{Style.RESET_ALL}
{Fore.CYAN}╠══════════════════════════════════════════════════════════════╣
║  21. Deep Scan (Run All)  │  0.  Exit                       ║
╚══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""
        print(menu)

    def run_deep_scan(self, target):
        """Run all modules for comprehensive scan"""
        self.print_info(f"Starting Deep Scan for: {target}")
        
        modules = [
            ("Instagram", self.instagram_osint),
            ("Facebook", self.facebook_osint),
            ("LinkedIn", self.linkedin_osint),
            ("Twitter", self.twitter_osint),
            ("YouTube", self.youtube_osint),
            ("GitHub", self.github_osint),
            ("Google Dorks", self.google_dork_search),
            ("Username Search", self.username_reverse_search),
            ("Pastebin", self.pastebin_scraper),
            ("Reddit", self.reddit_osint),
            ("Archive.org", self.archive_lookup),
        ]
        
        for name, func in modules:
            try:
                self.print_info(f"Running {name} module...")
                func(target)
                time.sleep(2)  # Be respectful to services
            except Exception as e:
                self.print_error(f"Error in {name} module: {e}")
        
        self.print_success("Deep Scan completed!")

    def main(self):
        """Main program loop"""
        self.print_banner()
        
        while True:
            self.show_menu()
            
            try:
                choice = input(f"\n{Fore.YELLOW}[?] Select your choice: {Style.RESET_ALL}").strip()
                
                if choice == "0":
                    self.print_success("Thanks for using SocialIntellax! Stay ethical! 🛡️")
                    break
                
                elif choice == "21":
                    target = input(f"{Fore.RED}[?] Enter target for Deep Scan: {Style.RESET_ALL}").strip()
                    if target:
                        self.run_deep_scan(target)
                    else:
                        self.print_error("Target cannot be empty")
                
                elif choice in [str(i) for i in range(1, 21)]:
                    target = input(f"{Fore.RED}[?] Enter target: {Style.RESET_ALL}").strip()
                    if not target:
                        self.print_error("Target cannot be empty")
                        continue
                    
                    # Module mapping
                    modules = {
                        "1": self.instagram_osint,
                        "2": self.facebook_osint,
                        "3": self.linkedin_osint,
                        "4": self.twitter_osint,
                        "5": self.youtube_osint,
                        "6": self.github_osint,
                        "7": self.google_dork_search,
                        "8": self.email_lookup,
                        "9": self.username_reverse_search,
                        "10": self.pastebin_scraper,
                        "11": self.darkweb_intel,
                        "12": self.geoip_lookup,
                        "13": self.metadata_extractor,
                        "14": self.reverse_image_search,
                        "15": self.phishing_url_check,
                        "16": self.mutuals_detector,
                        "17": self.reddit_osint,
                        "18": self.archive_lookup,
                        "19": self.company_dorks,
                        "20": self.discord_lookup,
                    }
                    
                    if choice in modules:
                        modules[choice](target)
                    
                else:
                    self.print_error("Invalid choice. Please try again.")
                
                input(f"\n{Fore.CYAN}Press Enter to continue...{Style.RESET_ALL}")
                
            except KeyboardInterrupt:
                self.print_warning("\nOperation cancelled by user")
                break
            except Exception as e:
                self.print_error(f"Unexpected error: {e}")

if __name__ == "__main__":
    try:
        # Check if required packages are available
        required_packages = {
            'requests': 'requests',
            'colorama': 'colorama',
            'beautifulsoup4': 'bs4',
            'tabulate': 'tabulate'
        }
        missing_packages = []

        for pkg_name, module_name in required_packages.items():
            try:
                __import__(module_name)
            except ImportError:
                missing_packages.append(pkg_name)

        if missing_packages:
            print(f"[91mMissing required packages: {', '.join(missing_packages)}")
            print(f"Install with: pip install {' '.join(missing_packages)}[0m")
            sys.exit(1)
        
        # Run the tool
        tool = SocialIntellax()
        tool.main()
        
    except Exception as e:
        print(f"{Fore.RED}Fatal error: {e}{Style.RESET_ALL}")
        sys.exit(1)
