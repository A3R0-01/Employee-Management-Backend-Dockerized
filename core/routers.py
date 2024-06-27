from rest_framework import routers
from core.company.viewset import CompanyViewset
from core.department.viewset import DepartmentViewset
from core.registration.viewset import RegistrationViewset
from core.employee.viewset import EmployeeViewset
from core.job.viewset import JobViewset
from core.role.viewset import RoleViewset, RoleTerminateViewset
from core.bulkEmployee.viewset import EmployeeBulk
router = routers.SimpleRouter()

router.register(r'company', CompanyViewset, basename='company')
router.register(r'department', DepartmentViewset, basename='department')
router.register(r'registration', RegistrationViewset, basename='registration')
router.register(r'employee', EmployeeViewset, basename='employee')
router.register(r'job', JobViewset, basename='job')
router.register(r'role', RoleViewset, basename='role')
router.register(r'role/terminate', RoleTerminateViewset, basename='terminate')
router.register(r'bulk/employee', EmployeeBulk, basename='bulk-employee')

urlpatterns = [
    *router.urls,
]