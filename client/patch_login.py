import re

with open("src/pages/Login.tsx", "r") as f:
    content = f.read()

content = content.replace(
    'import { useNavigate } from "react-router-dom";',
    'import { useNavigate } from "react-router-dom";\nimport { useAuth } from "@rhino-dev/rhino-react";'
)

new_submit = """    const { login, setOrganization } = useAuth()
    const [errorMsg, setErrorMsg] = useState("")
    
    const handleSubmit = async (e: React.FormEvent) => {
      e.preventDefault()
      setIsLoading(true)
      setErrorMsg("")
      
      const result = await login(email, password)
      if (!result.success) {
          setErrorMsg(result.error ?? "Login failed")
          setIsLoading(false)
          return
      }
      
      if (result.organization_slug) setOrganization(result.organization_slug)
      
      setSuccessMessage(`Authenticated. Redirecting...`)
      window.setTimeout(() => {
        setIsLoading(false)
        navigate("/")
      }, 600)
    }"""

content = re.sub(r'const handleSubmit = \(e\) => \{[\s\S]*?\}, 600\)\n    \}', new_submit, content)

content = content.replace(
    '{successMessage ? (',
    '{errorMsg ? (\n      <Alert className="bg-red-500/10 border-red-500/20 text-red-600 py-2.5">\n      <AlertDescription className="text-xs font-medium ml-2">{errorMsg}</AlertDescription>\n      </Alert>\n      ) : successMessage ? ('
)

with open("src/pages/Login.tsx", "w") as f:
    f.write(content)
