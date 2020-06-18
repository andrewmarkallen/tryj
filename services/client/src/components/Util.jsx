//  import * as R from 'ramda'

export const service_url = `${process.env.REACT_APP_USERS_SERVICE_URL}`

export const auth_json = () => {
  const a_j = {
    'Content-Type': 'application/json',
  }
  return a_j
}

export const axios_options = (url, method, headers=undefined,
                              data=undefined, queryString='')  => {
  const options = {
    url: `${service_url}${url}`,
    method: method,
    headers: headers,
  }
  if (data !== undefined) { options.data = data}
  if (headers !== undefined) { options.headers = auth_json()}
  if (queryString) {
    options.url = `${url}${queryString}`
    console.log(options)
  }
  return options
}
