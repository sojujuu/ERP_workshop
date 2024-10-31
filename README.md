# ERP workshop with Odoo
This repo contains odoo scafold for odoo workshop.
## Installation
1. Update workshop_1 wherever you want
2. Kick start docker by using this command
```
docker compose up
```
3. Modify existing container by using docker exec
```
docker compose exec odoo bash
```
4. Look up DB container by using docker exec
   
```
docker compose exec db psql -U odoo postgres
```

# Odoo Mini Project
This is what my team made as a mini-scale project at work.

```
class RoleBasedAccessControl:
    def _init_(self):
        # Dictionary untuk menyimpan izin akses per departemen
        self.permissions = {
            "HR": ["employee_data", "payroll"],
            "Finance": ["budget", "financial_reports"],
            "IT": ["system_logs", "security_settings"],
            "Sales": ["customer_data", "sales_reports"]
        }
    def grant_access(self, department, resource):
        # Menambah akses resource baru ke departemen
        if department in self.permissions:
            if resource not in self.permissions[department]:
                self.permissions[department].append(resource)
            else:
                print(f"{resource} sudah tersedia untuk {department}")
        else:
            print(f"Departemen {department} tidak ditemukan")
 
    def revoke_access(self, department, resource):
        # Menghapus akses resource dari departemen
        if department in self.permissions:
            if resource in self.permissions[department]:
                self.permissions[department].remove(resource)
            else:
                print(f"{resource} tidak tersedia untuk {department}")
        else:
            print(f"Departemen {department} tidak ditemukan")
    def check_access(self, department, resource):
        # Memeriksa apakah departemen memiliki akses ke resource tertentu
        if department in self.permissions and resource in self.permissions[department]:
            return True
        else:
            return False
 

# Implementasi Admin untuk menyesuaikan akses
class Admin:
    def _init_(self, rbac):
        self.rbac = rbac
    def adjust_access(self, department, resource, action):
        if action == "grant":
            self.rbac.grant_access(department, resource)
        elif action == "revoke":
            self.rbac.revoke_access(department, resource)
        else:
            print("Aksi tidak dikenali")
 

# Contoh penggunaan
rbac_system = RoleBasedAccessControl()
admin = Admin(rbac_system)
 
# Memberikan akses baru ke departemen IT
admin.adjust_access("IT", "network_settings", "grant")
 
# Mengecek akses
department = "IT"
resource = "network_settings"
if rbac_system.check_access(department, resource):
    print(f"{department} memiliki akses ke {resource}")
else:
    print(f"{department} tidak memiliki akses ke {resource}")
 
# Menghapus akses
admin.adjust_access("IT", "network_settings", "revoke")
```

