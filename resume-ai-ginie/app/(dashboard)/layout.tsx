import DashBoardBar from '@/components/DashboardBar'
import React from 'react'

const DashBoardBarLayout = ({children}: {children: React.ReactNode}) => {
  return (
    <>
      <DashBoardBar />
      {children}
    </>
  )
}

export default DashBoardBarLayout