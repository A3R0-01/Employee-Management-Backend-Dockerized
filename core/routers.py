from rest_framework import routers
from core.company.viewset import CompanyViewset, CompanyBulkViewset
from core.department.viewset import DepartmentViewset, DepartmentBulkViewset
from core.registration.viewset import RegistrationViewset, RegistrationBulkViewset
from core.employee.viewset import EmployeeViewset, EmployeeBulkViewset
from core.job.viewset import JobViewset, JobBulkViewset
from core.role.viewset import RoleViewset, RoleTerminateViewset, RoleBulkViewset
# from core.bulkEmployee.viewset import EmployeeBulk
router = routers.SimpleRouter()

router.register(r'company', CompanyViewset, basename='company')
router.register(r'department', DepartmentViewset, basename='department')
router.register(r'registration', RegistrationViewset, basename='registration')
router.register(r'employee', EmployeeViewset, basename='employee')
router.register(r'job', JobViewset, basename='job')
router.register(r'role', RoleViewset, basename='role')
router.register(r'role/terminate', RoleTerminateViewset, basename='terminate')
# router.register(r'bulk/employee', EmployeeBulk, basename='bulk-employee-test')


urlpatterns = [
    *router.urls,
]