from rest_framework import routers
from core.company.viewset import CompanyBulkViewset
from core.department.viewset import DepartmentBulkViewset
from core.registration.viewset import RegistrationBulkViewset
from core.employee.viewset import EmployeeBulkViewset
from core.job.viewset import JobBulkViewset
from core.role.viewset import RoleBulkViewset

router = routers.SimpleRouter()
router.register(r'company', CompanyBulkViewset, basename='bulk-company')
router.register(r'department', DepartmentBulkViewset, basename='bulk-department')
router.register(r'registration', RegistrationBulkViewset, basename='bulk-registration')
router.register(r'employee', EmployeeBulkViewset, basename='bulk-employee')
router.register(r'job', JobBulkViewset, basename='bulk-job')
router.register(r'role', RoleBulkViewset, basename='bulk-role')

bulkurlpatterns = [
    *router.urls,
]
